import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import List, Dict, Optional
import random

# SECURE API KEY HANDLING
ANTHROPIC_API_KEY = st.secrets["ANTHROPIC_API_KEY"]

st.set_page_config(page_title="PHL201 Epistemology - CognitiveCloud.ai", layout="wide", initial_sidebar_state="expanded")

# 40 epistemology-focused questions based on course readings
questions = [
    ("What is epistemology?", 
     ["The study of being and existence", "The attempt to determine what knowledge and truth are", "The study of ethics and morality", "The analysis of logical arguments"], 
     "The attempt to determine what knowledge and truth are"),
    
    ("According to the course readings, what is a philosophical claim?", 
     ["A statement about emotions", "A declarative sentence that can be true or false", "A question without an answer", "A religious belief"], 
     "A declarative sentence that can be true or false"),
    
    ("Stenstad distinguishes between theoretical and anarchic thinking. Theoretical thinking holds that:", 
     ["Multiple contradictory views can be true", "If one view is correct, different views must be incorrect", "All opinions are equally valid", "Truth is relative to culture"], 
     "If one view is correct, different views must be incorrect"),
    
    ("What makes a philosophical claim 'vague'?", 
     ["It's about abstract concepts", "It uses words that are not precise or whose boundaries are unclear", "It's controversial", "It's too complex"], 
     "It uses words that are not precise or whose boundaries are unclear"),
    
    ("An ambiguous claim is problematic because:", 
     ["It's necessarily false", "It can have several possible meanings", "It's too simple", "It requires advanced knowledge"], 
     "It can have several possible meanings"),
    
    ("How can we avoid vagueness in philosophical claims?", 
     ["Use more technical vocabulary", "Define important terms through examples, synonyms, or explanations", "Avoid difficult topics", "Only discuss proven facts"], 
     "Define important terms through examples, synonyms, or explanations"),
    
    ("What distinguishes philosophical arguments from mere opinions?", 
     ["They're always true", "They provide premises to support conclusions", "They're more popular", "They're easier to understand"], 
     "They provide premises to support conclusions"),
    
    ("In standard argument form, what comes after the premises?", 
     ["More premises", "The conclusion preceded by 'therefore'", "Questions", "Examples"], 
     "The conclusion preceded by 'therefore'"),
    
    ("The classical definition of knowledge is:", 
     ["True belief", "Justified true belief", "Certain belief", "Popular belief"], 
     "Justified true belief"),
    
    ("Rationalism emphasizes which source of knowledge?", 
     ["Sensory experience only", "Reason and logic", "Authority and tradition", "Intuition only"], 
     "Reason and logic"),
    
    ("Empiricism emphasizes which source of knowledge?", 
     ["Pure reason only", "Sensory experience and observation", "Divine revelation", "Mathematical proof"], 
     "Sensory experience and observation"),
    
    ("A priori knowledge is:", 
     ["Knowledge gained through experience", "Knowledge that can be known independently of experience", "Knowledge from authorities", "Knowledge that changes over time"], 
     "Knowledge that can be known independently of experience"),
    
    ("A posteriori knowledge requires:", 
     ["Pure reasoning only", "Experience and observation", "Mathematical proof", "Authority confirmation"], 
     "Experience and observation"),
    
    ("The problem of the criterion in epistemology refers to:", 
     ["Difficulty measuring knowledge", "The circular challenge of needing criteria for truth to establish criteria for truth", "The cost of education", "The time required for learning"], 
     "The circular challenge of needing criteria for truth to establish criteria for truth"),
    
    ("Skepticism in epistemology questions:", 
     ["Only religious beliefs", "Whether certain or any knowledge is possible", "Only scientific claims", "Only philosophical arguments"], 
     "Whether certain or any knowledge is possible"),
    
    ("According to course readings, why should philosophical claims be supported by arguments?", 
     ["To make them longer", "Because unsupported claims are inadequate in philosophy", "To confuse opponents", "To show intelligence"], 
     "Because unsupported claims are inadequate in philosophy"),
    
    ("What is the relationship between premises and conclusions in arguments?", 
     ["They're unrelated", "Premises provide logical support for conclusions", "Conclusions support premises", "They're the same thing"], 
     "Premises provide logical support for conclusions"),
    
    ("The correspondence theory of truth states that:", 
     ["Truth is what most people believe", "Truth consists in agreement of thoughts with reality", "Truth is whatever works", "Truth doesn't exist"], 
     "Truth consists in agreement of thoughts with reality"),
    
    ("According to the readings, what makes philosophy different from other fields?", 
     ["It only studies ancient texts", "It examines fundamental assumptions other fields take for granted", "It requires no evidence", "It focuses only on practical problems"], 
     "It examines fundamental assumptions other fields take for granted"),
    
    ("When evaluating knowledge claims, we should ask:", 
     ["Who said it?", "What evidence supports this and could it be explained differently?", "Is it popular?", "Is it simple?"], 
     "What evidence supports this and could it be explained differently?"),
    
    ("The distinction between knowledge and opinion matters because:", 
     ["Knowledge is more popular", "Knowledge has rational justification and corresponds to reality", "Knowledge is easier", "Knowledge never changes"], 
     "Knowledge has rational justification and corresponds to reality"),
    
    ("Why do philosophers emphasize clarity in their claims?", 
     ["To sound smarter", "Because vague or ambiguous claims cannot be properly evaluated for truth", "To make arguments longer", "To confuse opponents"], 
     "Because vague or ambiguous claims cannot be properly evaluated for truth"),
    
    ("The Gettier problem challenges:", 
     ["The existence of truth", "The classical definition of knowledge as justified true belief", "The possibility of belief", "The need for justification"], 
     "The classical definition of knowledge as justified true belief"),
    
    ("According to course readings, what is the main difference between anarchic and theoretical thinking?", 
     ["They study different subjects", "Anarchic thinking accepts multiple valid perspectives while theoretical seeks one correct view", "They use different methods", "One is ancient, one is modern"], 
     "Anarchic thinking accepts multiple valid perspectives while theoretical seeks one correct view"),
    
    ("In philosophical discourse, why are ad hominem arguments problematic?", 
     ["They're too complex", "They attack the person rather than addressing their arguments", "They take too long", "They require special training"], 
     "They attack the person rather than addressing their arguments"),
    
    ("The law of non-contradiction states that:", 
     ["Everything contradicts everything else", "Something cannot both be and not be in the same respect at the same time", "All contradictions are true", "Logic is impossible"], 
     "Something cannot both be and not be in the same respect at the same time"),
    
    ("What role do thought experiments play in epistemology?", 
     ["They prove theories", "They test our intuitions about knowledge and help clarify concepts", "They replace empirical evidence", "They are just entertainment"], 
     "They test our intuitions about knowledge and help clarify concepts"),
    
    ("Foundationalism in epistemology claims that:", 
     ["All beliefs are equally basic", "Some beliefs are basic and don't require justification from other beliefs", "No beliefs can be justified", "Only empirical beliefs count"], 
     "Some beliefs are basic and don't require justification from other beliefs"),
    
    ("Coherentism differs from foundationalism by arguing that:", 
     ["Only foundations matter", "Beliefs are justified by fitting coherently with other beliefs", "No justification is possible", "Only sensory experience matters"], 
     "Beliefs are justified by fitting coherently with other beliefs"),
    
    ("What is the main epistemological concern with skepticism?", 
     ["It's too optimistic", "It challenges whether we can have any knowledge at all", "It's not philosophical", "It accepts everything as true"], 
     "It challenges whether we can have any knowledge at all"),
    
    ("Reliabilism judges knowledge based on:", 
     ["Popular consensus", "Whether the belief-forming process is reliable", "Authority endorsement", "Emotional certainty"], 
     "Whether the belief-forming process is reliable"),
    
    ("What is internalism in epistemology?", 
     ["Knowledge comes from within", "The factors that justify belief must be accessible to the believer", "Only internal mental states exist", "External world is irrelevant"], 
     "The factors that justify belief must be accessible to the believer"),
    
    ("Externalism in epistemology holds that:", 
     ["Only external things exist", "Justification can depend on factors outside the believer's awareness", "Knowledge is impossible", "Only empirical knowledge counts"], 
     "Justification can depend on factors outside the believer's awareness"),
    
    ("According to the readings, what makes epistemology a central philosophical discipline?", 
     ["It's the oldest field", "It examines the very possibility and nature of knowledge itself", "It's the easiest to understand", "It doesn't require arguments"], 
     "It examines the very possibility and nature of knowledge itself"),
    
    ("The tripartite definition of knowledge requires:", 
     ["Only truth", "Belief, truth, and justification", "Only justification", "Only belief"], 
     "Belief, truth, and justification"),
    
    ("What is epistemic circularity?", 
     ["Using circular reasoning", "Using a source of knowledge to validate itself", "Avoiding all reasoning", "Only trusting authorities"], 
     "Using a source of knowledge to validate itself"),
    
    ("Modal epistemology deals with:", 
     ["Only necessary truths", "Knowledge of possibility and necessity", "Only empirical facts", "Only logical truths"], 
     "Knowledge of possibility and necessity"),
    
    ("What distinguishes knowledge from lucky guesses?", 
     ["Knowledge is always certain", "Knowledge has proper justification and isn't accidental", "Knowledge is more popular", "Knowledge is simpler"], 
     "Knowledge has proper justification and isn't accidental"),
    
    ("The value problem in epistemology asks:", 
     ["How much knowledge costs", "Why knowledge is more valuable than mere true belief", "Which knowledge is most important", "How to measure knowledge"], 
     "Why knowledge is more valuable than mere true belief"),
    
    ("According to course material, why is precise definition important in philosophy?", 
     ["To sound more academic", "Because imprecise claims cannot be properly evaluated", "To make arguments longer", "To confuse opponents"], 
     "Because imprecise claims cannot be properly evaluated")
]

# Session state for quiz control
if 'questions' not in st.session_state:
    st.session_state.questions = questions
if 'current' not in st.session_state:
    st.session_state.current = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'feedback' not in st.session_state:
    st.session_state.feedback = None
if 'selected_answer' not in st.session_state:
    st.session_state.selected_answer = None
if 'answered' not in st.session_state:
    st.session_state.answered = False

def show_question():
    """Display current question with enhanced UI"""
    if st.session_state.current < len(st.session_state.questions):
        q, opts, correct = st.session_state.questions[st.session_state.current]
        
        # Progress bar
        progress = (st.session_state.current + 1) / len(st.session_state.questions)
        st.progress(progress, text=f"Question {st.session_state.current + 1} of {len(st.session_state.questions)}")
        
        st.subheader(f"Question {st.session_state.current + 1}")
        st.write(f"**{q}**")
        
        # Radio button for answers
        if not st.session_state.answered:
            ans = st.radio("Choose your answer:", opts, key=f"q{st.session_state.current}")
            st.session_state.selected_answer = ans
            
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("Submit Answer", type="primary"):
                    if ans == correct:
                        st.session_state.feedback = ("success", "Correct! +10 XP")
                        st.session_state.score += 10
                    else:
                        st.session_state.feedback = ("error", f"Incorrect. The answer is: **{correct}**")
                    st.session_state.answered = True
                    st.rerun()
        else:
            # Show the question and selected answer when answered
            st.write(f"**Your answer:** {st.session_state.selected_answer}")
            show_feedback()
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Next Question", type="primary"):
                    st.session_state.current += 1
                    st.session_state.answered = False
                    st.session_state.feedback = None
                    st.session_state.selected_answer = None
                    st.rerun()
            with col2:
                if st.button("Skip to End"):
                    st.session_state.current = len(st.session_state.questions)
                    st.rerun()

def show_feedback():
    """Display feedback with enhanced styling"""
    if st.session_state.feedback:
        typ, msg = st.session_state.feedback
        if typ == "success":
            st.success(msg)
        else:
            st.error(msg)

def show_score():
    """Display current score with styling"""
    col1, col2, col3 = st.columns(3)
    with col2:
        st.metric("Current Score", f"{st.session_state.score} XP", 
                 delta=f"{st.session_state.current} answered")

def restart_quiz():
    """Reset quiz state"""
    if st.button("Restart Assessment", type="secondary"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.feedback = None
        st.session_state.selected_answer = None
        st.session_state.answered = False
        st.rerun()

def create_visualizations():
    """Create philosophical concept visualizations"""
    st.header("Epistemological Concept Visualizations")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Argument Structure", "Knowledge Sources", "JTB Analysis", "Epistemological Theories"])
    
    with tab1:
        st.subheader("Philosophical Argument Structure")
        
        # Argument visualization
        fig = go.Figure()
        
        # Premises flowing to conclusion
        fig.add_shape(type="rect", x0=1, y0=3, x1=3, y1=4, 
                     fillcolor="lightblue", line=dict(color="blue"))
        fig.add_annotation(x=2, y=3.5, text="Premise 1", showarrow=False, font=dict(size=12))
        
        fig.add_shape(type="rect", x0=1, y0=2, x1=3, y1=3, 
                     fillcolor="lightblue", line=dict(color="blue"))
        fig.add_annotation(x=2, y=2.5, text="Premise 2", showarrow=False, font=dict(size=12))
        
        # Arrow pointing to conclusion
        fig.add_annotation(x=2, y=1.7, ax=2, ay=2, 
                          arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="red")
        
        fig.add_shape(type="rect", x0=1, y0=0.5, x1=3, y1=1.5, 
                     fillcolor="lightcoral", line=dict(color="red"))
        fig.add_annotation(x=2, y=1, text="Therefore:<br>Conclusion", showarrow=False, font=dict(size=12))
        
        fig.update_layout(
            title="Standard Argument Form",
            xaxis=dict(range=[0, 4], showgrid=False, showticklabels=False),
            yaxis=dict(range=[0, 5], showgrid=False, showticklabels=False),
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("**Key Insight**: Valid arguments have premises that logically support their conclusions. The structure matters as much as the content.")
    
    with tab2:
        st.subheader("Sources of Knowledge in Epistemology")
        
        # Knowledge sources pie chart
        sources = ['Sensory Experience (Empiricism)', 'Reason & Logic (Rationalism)', 
                  'Intuition', 'Authority', 'Testimony']
        values = [35, 30, 15, 12, 8]
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
        
        fig = go.Figure(data=[go.Pie(labels=sources, values=values, hole=.3)])
        fig.update_traces(hoverinfo="label+percent", textinfo="label+percent", 
                         textfont_size=10, marker=dict(colors=colors))
        fig.update_layout(title="Epistemological Sources of Knowledge", height=500)
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Rationalism**: Knowledge primarily through reason (Plato, Descartes)
        
        **Empiricism**: Knowledge primarily through sensory experience (Aristotle, Hume)
        
        **Critical Question**: How do we determine which source is most reliable?
        """)
    
    with tab3:
        st.subheader("JTB Analysis of Knowledge")
        
        # Create Venn diagram-style visualization for JTB
        fig = go.Figure()
        
        # Three overlapping circles for Justification, Truth, Belief
        fig.add_shape(type="circle", x0=0, y0=1, x1=2, y1=3, 
                     fillcolor="rgba(255, 0, 0, 0.3)", line=dict(color="red"))
        fig.add_annotation(x=0.5, y=2.5, text="Belief", showarrow=False, font=dict(size=14))
        
        fig.add_shape(type="circle", x0=1.5, y0=1, x1=3.5, y1=3, 
                     fillcolor="rgba(0, 255, 0, 0.3)", line=dict(color="green"))
        fig.add_annotation(x=3, y=2.5, text="Truth", showarrow=False, font=dict(size=14))
        
        fig.add_shape(type="circle", x0=0.75, y0=0, x1=2.75, y1=2, 
                     fillcolor="rgba(0, 0, 255, 0.3)", line=dict(color="blue"))
        fig.add_annotation(x=1.75, y=0.5, text="Justification", showarrow=False, font=dict(size=14))
        
        # Center intersection
        fig.add_annotation(x=1.75, y=1.8, text="KNOWLEDGE<br>(JTB)", showarrow=False, 
                          font=dict(size=12, color="black"), 
                          bgcolor="yellow", bordercolor="black", borderwidth=2)
        
        fig.update_layout(
            title="Classical Analysis: Knowledge as Justified True Belief",
            xaxis=dict(range=[-0.5, 4], showgrid=False, showticklabels=False),
            yaxis=dict(range=[-0.5, 3.5], showgrid=False, showticklabels=False),
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("**The Gettier Problem**: Cases where someone has justified true belief but intuitively lacks knowledge, challenging this classical analysis.")
    
    with tab4:
        st.subheader("Major Epistemological Theories Timeline")
        
        theories = [
            ("Classical Foundationalism", 1600, "Descartes - Certain foundations"),
            ("Empiricism", 1650, "Locke - Experience as source"),
            ("Skepticism", 1700, "Hume - Limits of knowledge"),
            ("JTB Analysis", 1900, "Traditional definition"),
            ("Gettier Problem", 1963, "Challenge to JTB"),
            ("Reliabilism", 1970, "Reliable processes"),
            ("Virtue Epistemology", 1980, "Intellectual virtues"),
            ("Contextualism", 1990, "Context-sensitive knowledge")
        ]
        
        fig = go.Figure()
        
        for i, (theory, year, description) in enumerate(theories):
            fig.add_trace(go.Scatter(
                x=[year], y=[i], 
                mode='markers+text',
                text=[theory], 
                textposition="middle right",
                marker=dict(size=15, color='blue'),
                name=theory,
                hovertext=f"{theory} ({year}): {description}"
            ))
        
        fig.update_layout(
            title="Development of Epistemological Theories",
            xaxis_title="Year",
            yaxis=dict(showticklabels=False),
            height=500,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("This timeline shows how epistemological theories have evolved in response to problems with earlier approaches.")

# Main Application Layout
st.title("PHL201 Epistemology - CognitiveCloud.ai")
st.markdown("**Interactive Epistemology Learning Platform | Developed by Xavier Honablue M.Ed**")

# Sidebar for navigation
with st.sidebar:
    st.header("Course Navigation")
    page = st.radio("Choose Section:", [
        "Course Introduction", 
        "Core Epistemology Modules",
        "Knowledge Assessment", 
        "Concept Visualizations", 
        "Quick Reference",
        "Resources & Links",
        "Epistemology AI Tutor",
        "Reflection Discussions"
    ])
    
    st.markdown("---")
    st.subheader("Your Progress")
    if st.session_state.questions:
        progress_pct = (st.session_state.current / len(st.session_state.questions)) * 100
        st.metric("Assessment Progress", f"{progress_pct:.1f}%")
        st.metric("Knowledge Points", f"{st.session_state.score} XP")

# Main content based on page selection
if page == "Course Introduction":
    st.header("PHL201: Introduction to Epistemology")
    st.markdown("**Developed by Xavier Honablue M.Ed | CognitiveCloud.ai**")
    
    st.markdown("""
    ## What is Epistemology?
    
    Epistemology is the branch of philosophy that investigates the nature, sources, and limits of human knowledge. 
    As our course readings explain, it addresses fundamental questions about what we can know and how we can know it.
    
    ## Core Course Themes
    
    **The Nature of Knowledge:**
    - What distinguishes knowledge from mere opinion or belief?
    - How do we analyze the classical definition: justified true belief?
    - What challenges does the Gettier problem pose to our understanding?
    
    **Sources and Methods of Knowledge:**
    - Rationalism vs. Empiricism: reason versus experience
    - A priori vs. a posteriori knowledge
    - The roles of perception, memory, and testimony
    
    **Philosophical Reasoning:**
    - How to construct and evaluate philosophical arguments
    - Avoiding vague and ambiguous claims (as discussed in course readings)
    - Supporting claims with premises and conclusions
    
    **Epistemological Problems:**
    - The problem of the criterion
    - Skeptical challenges to knowledge
    - Foundationalism vs. coherentism
    - The relationship between theoretical and anarchic thinking
    
    ## Learning Objectives
    
    By the end of this course, you will be able to:
    
    1. **Analyze** the concept of knowledge and distinguish it from belief and opinion
    2. **Evaluate** different theories about the sources and justification of knowledge
    3. **Construct** clear philosophical arguments following standard form
    4. **Apply** epistemological concepts to real-world knowledge claims
    5. **Discuss** major epistemological problems and proposed solutions
    
    ## Course Structure
    
    **Core Modules**: Deep dives into fundamental epistemological concepts
    
    **Assessments**: Test your understanding with targeted questions
    
    **Visualizations**: See epistemological relationships and structures
    
    **AI Tutor**: Get personalized help with difficult concepts
    
    **Discussions**: Engage with reflection questions connected to course readings
    
    ## About the Instructor
    
    **Xavier Honablue, M.Ed** brings expertise in educational technology and philosophical pedagogy to create 
    an engaging, interactive learning experience that bridges traditional epistemology with modern learning methods.
    
    ---
    
    *Ready to explore the fascinating world of knowledge and truth? Start with the Core Epistemology Modules!*
    """)

elif page == "Core Epistemology Modules":
    st.header("Core Epistemology Learning Modules")
    
    module = st.selectbox("Choose a learning module:", [
        "Module 1: What is Epistemology?",
        "Module 2: Philosophical Claims and Arguments", 
        "Module 3: Knowledge vs. Belief and Opinion",
        "Module 4: The Classical Definition of Knowledge (JTB)",
        "Module 5: The Gettier Problem and Beyond"
    ])
    
    if module == "Module 1: What is Epistemology?":
        st.subheader("What is Epistemology?")
        
        st.markdown("""
        ## The Theory of Knowledge
        
        **Epistemology** is the branch of philosophy that investigates the nature, sources, and limits of human knowledge. 
        As our course readings explain, it attempts to determine what knowledge and truth are, addressing some of the most 
        fundamental questions humans can ask.
        
        ## Central Epistemological Questions
        
        **The Nature Question**: What is knowledge? How does it differ from mere belief or opinion?
        
        **The Sources Question**: Where does knowledge come from? Do we gain knowledge primarily through:
        - Sensory experience and observation?
        - Reason and logical thinking?
        - Intuition or insight?
        - Authority and testimony?
        
        **The Limits Question**: What can we know? Are there things that are unknowable in principle?
        
        **The Justification Question**: What makes a belief justified? When are we entitled to claim we know something?
        
        ## Why Epistemology Matters
        
        Epistemology isn't just abstract philosophical speculation. It has practical implications for:
        
        **Science**: How do we distinguish genuine scientific knowledge from pseudoscience?
        
        **Education**: What should we teach, and how do we know it's true?
        
        **Decision-Making**: How much evidence do we need before acting on a belief?
        
        **Democracy**: How do citizens evaluate competing claims from experts and authorities?
        """)
        
        with st.expander("Reflection Questions"):
            st.markdown("""
            **Consider these questions:**
            1. What's something you're confident you know? What makes you confident?
            2. How do you typically decide whether to believe a claim you encounter online or in the news?
            3. Is there a difference between knowing something and being certain about it?
            4. Can you think of beliefs you once held confidently but now reject? What changed?
            """)
    
    elif module == "Module 2: Philosophical Claims and Arguments":
        st.subheader("Philosophical Claims and Arguments")
        
        st.markdown("""
        ## What are Philosophical Claims?
        
        As discussed in our course readings, a **philosophical claim** is a declarative sentence or statement that can be true or false. 
        Philosophy proceeds by making, examining, and evaluating such claims.
        
        **Examples of epistemological claims:**
        - "Knowledge requires justified true belief"
        - "Sensory experience is the primary source of knowledge"
        - "We cannot have certain knowledge about the external world"
        - "All knowledge ultimately depends on assumptions we cannot prove"
        
        ## The Problem of Vagueness
        
        Our readings emphasize that **vague claims** use words that are not precise or whose boundaries are unclear. 
        This creates problems because we cannot properly evaluate claims if we don't know exactly what they mean.
        
        **Example**: "Older people shouldn't drive"
        - How old is "older"? 65? 70? 80?
        - What about exceptions for healthy, skilled elderly drivers?
        - Does this apply to all driving or just certain conditions?
        
        ## The Problem of Ambiguity
        
        **Ambiguous claims** use words that can have several possible meanings. This makes it impossible to determine 
        what the claim actually asserts.
        
        **Example**: "The bank is closed"
        - Financial institution or river bank?
        - Temporarily closed or permanently?
        
        ## Solutions: Achieving Clarity
        
        **Three ways to define unclear terms:**
        
        **1. Examples**: Define "empirical knowledge" by listing: scientific observations, sensory experiences, experimental results, etc.
        
        **2. Synonyms**: Define "a priori knowledge" as "knowledge independent of experience"
        
        **3. Explanations**: Provide a clear analytical definition. For example: "Justified belief is a belief held on the basis of good reasons that make the belief likely to be true"
        
        ## Philosophical Arguments
        
        Philosophy doesn't just make claims - it provides **arguments** to support them. An argument consists of:
        
        **Premises**: Statements that provide evidence or reasons
        **Conclusion**: The statement the premises are meant to support
        """)
    
    elif module == "Module 3: Knowledge vs. Belief and Opinion":
        st.subheader("Knowledge vs. Belief and Opinion")
        
        st.markdown("""
        ## The Fundamental Distinction
        
        One of epistemology's most important tasks is distinguishing between what we actually **know** and what we merely **believe** or **think we know**. 
        This distinction has practical importance for science, education, law, and everyday decision-making.
        
        ## Characteristics of Knowledge
        
        **Traditional Requirements for Knowledge:**
        
        **1. Truth**:
