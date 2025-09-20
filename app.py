import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import List, Dict, Optional
import random

# 🔐 SECURE API KEY HANDLING
ANTHROPIC_API_KEY = st.secrets["ANTHROPIC_API_KEY"]

st.set_page_config(page_title="Philosophy Foundations & Epistemology CognitiveCloud.ai", layout="wide", initial_sidebar_state="expanded")

# 35 comprehensive philosophy questions
questions = [
    ("What is the primary purpose of philosophy?", 
     ["To memorize historical facts", "To examine fundamental questions about reality, knowledge, and existence", "To debate politics", "To study literature"], 
     "To examine fundamental questions about reality, knowledge, and existence"),
    
    ("A philosophical claim must be:", 
     ["Always true", "A statement that can be either true or false", "An opinion without evidence", "A religious belief"], 
     "A statement that can be either true or false"),
    
    ("What makes a claim 'vague' in philosophical terms?", 
     ["It uses complex vocabulary", "It uses words that are not precise or whose boundaries are unclear", "It disagrees with common opinion", "It refers to abstract concepts"], 
     "It uses words that are not precise or whose boundaries are unclear"),
    
    ("An ambiguous claim is one that:", 
     ["Is definitely false", "Uses words that can have several possible meanings", "Is too simple", "Cannot be understood"], 
     "Uses words that can have several possible meanings"),
    
    ("What is epistemology?", 
     ["The study of being and existence", "The attempt to determine what knowledge and truth are", "The study of ethics and morality", "The analysis of logical arguments"], 
     "The attempt to determine what knowledge and truth are"),
    
    ("A philosophical argument consists of:", 
     ["Only a conclusion", "Premises and a conclusion together", "Questions without answers", "Emotional appeals"], 
     "Premises and a conclusion together"),
    
    ("How can we avoid vagueness in philosophical claims?", 
     ["Use more complex language", "Define important terms through examples, synonyms, or clear explanations", "Avoid difficult topics", "Only discuss well-known ideas"], 
     "Define important terms through examples, synonyms, or clear explanations"),
    
    ("Thales is important to Western philosophy because he:", 
     ["Wrote the first philosophy textbook", "Was the first to seek natural rather than supernatural explanations", "Founded the first university", "Discovered mathematics"], 
     "Was the first to seek natural rather than supernatural explanations"),
    
    ("According to Thales, what is the fundamental substance of all things?", 
     ["Fire", "Air", "Water", "Earth"], 
     "Water"),
    
    ("Heraclitus believed that the fundamental nature of reality is:", 
     ["Permanent and unchanging", "Constant change and flux", "Mathematical in nature", "Purely spiritual"], 
     "Constant change and flux"),
    
    ("Heraclitus's famous statement 'You cannot step into the same river twice' illustrates:", 
     ["The permanence of nature", "The reality of constant change", "The importance of water", "The difficulty of travel"], 
     "The reality of constant change"),
    
    ("Parmenides argued that:", 
     ["Everything is constantly changing", "Change is an illusion and reality is permanent and unified", "Knowledge is impossible", "Only mathematics is real"], 
     "Change is an illusion and reality is permanent and unified"),
    
    ("Zeno's paradoxes were designed to:", 
     ["Prove that mathematics is false", "Support Parmenides' view that motion and change are impossible", "Show that time doesn't exist", "Demonstrate the power of logic"], 
     "Support Parmenides' view that motion and change are impossible"),
    
    ("In Zeno's paradox of Achilles and the tortoise:", 
     ["Achilles can never catch the tortoise because he must always reach where the tortoise was", "Achilles easily wins the race", "The tortoise moves faster than Achilles", "Distance is an illusion"], 
     "Achilles can never catch the tortoise because he must always reach where the tortoise was"),
    
    ("The Upanishads teach that:", 
     ["Individual souls are separate from ultimate reality", "Individual souls (Atman) are identical with ultimate reality (Brahman)", "Knowledge is impossible", "Only gods can understand truth"], 
     "Individual souls (Atman) are identical with ultimate reality (Brahman)"),
    
    ("The statement 'That art thou' (Tat tvam asi) means:", 
     ["You are separate from the divine", "You are identical with the ultimate reality of the universe", "You cannot know the truth", "You must worship external gods"], 
     "You are identical with the ultimate reality of the universe"),
    
    ("The Pre-Socratic philosophers were primarily concerned with:", 
     ["Political theory", "Discovering the ultimate constituents and nature of reality", "Religious practices", "Artistic expression"], 
     "Discovering the ultimate constituents and nature of reality"),
    
    ("What distinguishes philosophy from mythology in explaining natural phenomena?", 
     ["Philosophy is older than mythology", "Philosophy seeks natural, rational explanations rather than supernatural ones", "Philosophy is easier to understand", "Philosophy doesn't ask questions"], 
     "Philosophy seeks natural, rational explanations rather than supernatural ones"),
    
    ("In constructing philosophical arguments, premises should:", 
     ["Always be controversial", "Provide logical support for the conclusion", "Be based on emotion", "Avoid evidence"], 
     "Provide logical support for the conclusion"),
    
    ("When we put an argument in 'standard form,' we:", 
     ["Make it more confusing", "List the premises first, then the conclusion with 'therefore'", "Remove all logic", "Add emotional appeals"], 
     "List the premises first, then the conclusion with 'therefore'"),
    
    ("What is the difference between theoretical and anarchic thinking (as discussed in epistemology)?", 
     ["They study different subjects", "Theoretical thinking seeks one correct view; anarchic thinking accepts multiple valid perspectives", "They use different languages", "One is ancient, one is modern"], 
     "Theoretical thinking seeks one correct view; anarchic thinking accepts multiple valid perspectives"),
    
    ("The concept that 'being and truth are convertible' means:", 
     ["They are completely different", "Reality and our thinking about it share the same underlying structure", "Truth doesn't exist", "Being is purely mental"], 
     "Reality and our thinking about it share the same underlying structure"),
    
    ("What makes philosophy different from other academic disciplines?", 
     ["It only studies ancient texts", "It examines the fundamental assumptions that other fields take for granted", "It requires no reasoning", "It focuses only on practical problems"], 
     "It examines the fundamental assumptions that other fields take for granted"),
    
    ("Epistemological questions primarily concern:", 
     ["What exists in the physical world", "What we can know and how we can know it", "What we should do morally", "How governments should be organized"], 
     "What we can know and how we can know it"),
    
    ("The philosophical method emphasizes:", 
     ["Accepting traditional authorities without question", "Critical examination and reasoned argument", "Emotional responses only", "Practical applications without theory"], 
     "Critical examination and reasoned argument"),
    
    ("According to philosophical tradition, knowledge differs from mere opinion because:", 
     ["Knowledge is always practical", "Knowledge has rational justification and corresponds to reality", "Knowledge is more popular", "Knowledge changes constantly"], 
     "Knowledge has rational justification and corresponds to reality"),
    
    ("The problem of the criterion in epistemology refers to:", 
     ["Difficulty in measuring knowledge", "The circular challenge of needing criteria for truth to establish criteria for truth", "The cost of education", "The time required for learning"], 
     "The circular challenge of needing criteria for truth to establish criteria for truth"),
    
    ("In philosophical discourse, ad hominem arguments are problematic because they:", 
     ["Are too complex", "Attack the person rather than addressing their arguments", "Take too much time", "Require advanced education"], 
     "Attack the person rather than addressing their arguments"),
    
    ("The law of non-contradiction states that:", 
     ["Everything is contradictory", "Something cannot both be and not be in the same respect at the same time", "Contradictions are always true", "Logic is impossible"], 
     "Something cannot both be and not be in the same respect at the same time"),
    
    ("Skepticism in philosophy refers to:", 
     ["Accepting everything as true", "Questioning whether certain or any knowledge is possible", "Believing only in science", "Rejecting all questions"], 
     "Questioning whether certain or any knowledge is possible"),
    
    ("The correspondence theory of truth holds that:", 
     ["Truth is what most people believe", "Truth consists in the agreement of our thoughts with reality", "Truth is whatever works practically", "Truth doesn't exist"], 
     "Truth consists in the agreement of our thoughts with reality"),
    
    ("Rationalism in epistemology emphasizes:", 
     ["Only emotional knowledge", "Reason and logic as primary sources of knowledge", "Only sensory experience", "Random guessing"], 
     "Reason and logic as primary sources of knowledge"),
    
    ("Empiricism in epistemology emphasizes:", 
     ["Only logical reasoning", "Sensory experience as the primary source of knowledge", "Divine revelation", "Mathematical proof only"], 
     "Sensory experience as the primary source of knowledge"),
    
    ("The philosophical concept of 'a priori' knowledge refers to:", 
     ["Knowledge gained after experience", "Knowledge that can be known independently of experience", "Knowledge that requires tools", "Knowledge from authorities"], 
     "Knowledge that can be known independently of experience"),
    
    ("What is the fundamental insight of the philosophical revolution begun by Thales?", 
     ["Religious explanations are always correct", "Natural phenomena can be explained through rational inquiry rather than mythology", "Mathematics is the only true knowledge", "Human knowledge is impossible"], 
     "Natural phenomena can be explained through rational inquiry rather than mythology")
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
                        st.session_state.feedback = ("success", "✅ Correct! +10 XP")
                        st.session_state.score += 10
                    else:
                        st.session_state.feedback = ("error", f"❌ Incorrect. The answer is: **{correct}**")
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
    if st.button("🔄 Restart Quiz", type="secondary"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.feedback = None
        st.session_state.selected_answer = None
        st.session_state.answered = False
        st.rerun()

def create_visualizations():
    """Create philosophical concept visualizations"""
    st.header("📊 Philosophy Concept Visualizations")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Argument Structure", "Knowledge Sources", "Early Philosophers Timeline", "Epistemological Concepts"])
    
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
        fig.add_annotation(x=2, y=1, text="Therefore:\nConclusion", showarrow=False, font=dict(size=12))
        
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
                  'Intuition', 'Authority', 'Revelation']
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
        st.subheader("Early Philosophers Timeline")
        
        philosophers = [
            ("Thales", -624, "Water is the fundamental substance"),
            ("Heraclitus", -535, "Everything flows - constant change"),
            ("Parmenides", -515, "Change is illusion - Being is One"),
            ("Zeno", -490, "Paradoxes supporting Parmenides"),
            ("Democritus", -460, "Atomic theory of matter")
        ]
        
        fig = go.Figure()
        
        for i, (name, year, idea) in enumerate(philosophers):
            fig.add_trace(go.Scatter(
                x=[year], y=[i], 
                mode='markers+text',
                text=[name], 
                textposition="middle right",
                marker=dict(size=15, color='blue'),
                name=name,
                hovertext=f"{name} ({year} BCE): {idea}"
            ))
        
        fig.update_layout(
            title="Pre-Socratic Philosophers Timeline",
            xaxis_title="Year (BCE)",
            yaxis=dict(showticklabels=False),
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("These thinkers began the shift from mythological to rational explanations of natural phenomena.")
    
    with tab4:
        st.subheader("Epistemological Concepts Network")
        
        # Create a network-style visualization of epistemological concepts
        concepts = ['Knowledge', 'Truth', 'Belief', 'Justification', 'Skepticism', 'Certainty']
        
        # Create positions for concepts in a circle
        angles = np.linspace(0, 2*np.pi, len(concepts), endpoint=False)
        x_pos = np.cos(angles)
        y_pos = np.sin(angles)
        
        fig = go.Figure()
        
        # Add nodes
        fig.add_trace(go.Scatter(
            x=x_pos, y=y_pos,
            mode='markers+text',
            text=concepts,
            textposition="middle center",
            marker=dict(size=60, color='lightblue', line=dict(width=2, color='blue')),
            name="Concepts"
        ))
        
        # Add connections between related concepts
        connections = [(0,1), (0,2), (0,3), (1,3), (2,3), (4,0), (5,1)]
        for start, end in connections:
            fig.add_trace(go.Scatter(
                x=[x_pos[start], x_pos[end]], 
                y=[y_pos[start], y_pos[end]],
                mode='lines',
                line=dict(width=1, color='gray'),
                showlegend=False
            ))
        
        fig.update_layout(
            title="Interconnected Epistemological Concepts",
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False),
            height=500,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Central Question**: What is the relationship between knowledge, truth, and justified belief?
        
        **Classical Definition**: Knowledge = Justified True Belief (+ Gettier conditions)
        """)

# Main Application Layout
st.title("🧠 Philosophy Foundations & Epistemology CognitiveCloud.ai")
st.markdown("**Comprehensive Interactive Philosophy Learning Platform**")

# Sidebar for navigation
with st.sidebar:
    st.header("📚 Navigation")
    page = st.radio("Choose Section:", [
        "Course Overview", 
        "📖 Learning Modules",
        "🎯 Interactive Quiz", 
        "📊 Visualizations", 
        "📚 Reference Guide",
        "🔗 Resources & Links",
        "🤖 AI Philosophy Tutor"
    ])
    
    st.markdown("---")
    st.subheader("📈 Your Progress")
    if st.session_state.questions:
        progress_pct = (st.session_state.current / len(st.session_state.questions)) * 100
        st.metric("Quiz Completion", f"{progress_pct:.1f}%")
        st.metric("Score", f"{st.session_state.score} XP")

# Main content based on page selection
if page == "Course Overview":
    st.header("🌟 Philosophy Foundations & Epistemology")
    
    st.markdown("""
    Welcome to your comprehensive introduction to philosophical thinking and the theory of knowledge!
    
    ## 🎯 What You'll Learn
    
    **Core Philosophy Skills:**
    - How to identify and construct valid philosophical arguments
    - How to avoid vague and ambiguous claims
    - How to think critically about fundamental questions
    - How to distinguish philosophy from other fields of inquiry
    
    **Epistemology - The Theory of Knowledge:**
    - What is knowledge and how does it differ from opinion?
    - What are the sources of human knowledge?
    - How can we determine what is true?
    - What are the limits of human knowledge?
    
    **Historical Foundations:**
    - The Pre-Socratic revolution: from myth to rational inquiry
    - Thales and the search for natural explanations
    - Heraclitus vs. Parmenides: change vs. permanence
    - Eastern philosophy: the Upanishads and ultimate reality
    
    ## 🔍 Key Philosophical Questions
    
    This course addresses fundamental questions that humans have pondered for millennia:
    - What can we really know about reality?
    - How should we distinguish truth from opinion?
    - What is the relationship between thinking and being?
    - How do we construct valid arguments?
    
    ## 📚 Learning Path
    
    1. **Start with Learning Modules** - Master core concepts
    2. **Take the Interactive Quiz** - Test your understanding
    3. **Explore Visualizations** - See concepts in action
    4. **Use the Reference Guide** - Quick lookup of key terms
    5. **Chat with AI Tutor** - Get personalized help
    """)

elif page == "📖 Learning Modules":
    st.header("📖 Core Learning Modules")
    
    module = st.selectbox("Choose a learning module:", [
        "Module 1: What is Philosophy?",
        "Module 2: Critical Thinking & Arguments", 
        "Module 3: Epistemology - Theory of Knowledge",
        "Module 4: Pre-Socratic Philosophers",
        "Module 5: Knowledge vs. Opinion",
        "Module 6: Eastern Philosophy - The Upanishads"
    ])
    
    if module == "Module 1: What is Philosophy?":
        st.subheader("What is Philosophy?")
        
        st.markdown("""
        ## Definition and Purpose
        
        Philosophy is the systematic examination of fundamental questions about reality, knowledge, values, reason, mind, and existence. Unlike other academic disciplines that study specific aspects of the world, philosophy examines the basic assumptions that underlie all human inquiry.
        
        ## What Makes Philosophy Unique?
        
        **Philosophy differs from other fields because it:**
        - Questions assumptions that other disciplines take for granted
        - Uses rational argument and critical analysis as primary methods
        - Addresses questions that cannot be answered by empirical observation alone
        - Seeks to understand the most fundamental aspects of existence
        
        ## Core Areas of Philosophy
        
        **Metaphysics**: What exists? What is the nature of reality?
        
        **Epistemology**: What can we know? How do we know it?
        
        **Ethics**: What should we do? What makes actions right or wrong?
        
        **Logic**: What makes arguments valid? How should we reason?
        
        **Aesthetics**: What is beauty? What makes art valuable?
        
        ## The Philosophical Method
        
        Philosophy proceeds through:
        1. **Careful analysis** of concepts and arguments
        2. **Critical evaluation** of claims and reasoning
        3. **Systematic construction** of theories and explanations
        4. **Rigorous testing** of ideas through debate and reflection
        
        ## Why Study Philosophy?
        
        Philosophy develops critical thinking skills essential for:
        - Analyzing complex problems in any field
        - Evaluating arguments and evidence
        - Clarifying concepts and assumptions
        - Understanding the foundations of knowledge and ethics
        """)
        
        with st.expander("💡 Practice Questions"):
            st.markdown("""
            **Reflection Questions:**
            1. How does philosophy differ from science in its approach to understanding reality?
            2. What assumptions do you make in your daily life that philosophy might question?
            3. Why might it be important to examine our fundamental beliefs?
            """)
    
    elif module == "Module 2: Critical Thinking & Arguments":
        st.subheader("Critical Thinking & Philosophical Arguments")
        
        st.markdown("""
        ## Philosophical Claims
        
        A **philosophical claim** is a statement that can be either true or false. Philosophy proceeds by making, examining, and evaluating such claims.
        
        **Examples of philosophical claims:**
        - "Knowledge requires justified true belief"
        - "Reality is fundamentally mental rather than physical"
        - "Free will is incompatible with determinism"
        
        ## Problems: Vagueness and Ambiguity
        
        **Vague claims** use words that are not precise or whose boundaries are unclear.
        - Example: "Old people should not drive" (How old is "old"?)
        
        **Ambiguous claims** use words that can have several possible meanings.
        - Example: "The bank is closed" (Financial institution or river bank?)
        
        ## Solutions: Achieving Clarity
        
        **Three ways to define unclear terms:**
        
        1. **Examples**: Define "furniture" by listing tables, chairs, desks, etc.
        2. **Synonyms**: Define "canine" as "dog"
        3. **Explanations**: Provide a clear statement of what the term means
        
        ## Philosophical Arguments
        
        An **argument** consists of:
        - **Premises**: Statements that provide evidence or reasons
        - **Conclusion**: The statement the premises are meant to support
        
        **Standard Form Example:**
        ```
        Premise 1: All humans are mortal
        Premise 2: Socrates is human
        Therefore: Socrates is mortal
        ```
        
        ## Evaluating Arguments
        
        **Valid arguments**: The conclusion follows logically from the premises
        
        **Sound arguments**: Valid arguments with true premises
        
        **Common errors to avoid:**
        - Ad hominem attacks (attacking the person, not the argument)
        - Circular reasoning (using the conclusion to support itself)
        - False dichotomy (presenting only two options when more exist)
        """)
        
        with st.expander("💡 Practice Exercise"):
            st.markdown("""
            **Identify the premises and conclusion:**
            
            "Since philosophy examines fundamental assumptions, and other disciplines take these assumptions for granted, philosophy must be different from other academic fields."
            
            **Answer:**
            - Premise 1: Philosophy examines fundamental assumptions
            - Premise 2: Other disciplines take these assumptions for granted  
            - Conclusion: Philosophy is different from other academic fields
            """)
    
    elif module == "Module 3: Epistemology - Theory of Knowledge":
        st.subheader("Epistemology: The Theory of Knowledge")
        
        st.markdown("""
        ## What is Epistemology?
        
        **Epistemology** is the branch of philosophy that investigates the nature, sources, and limits of human knowledge. It asks fundamental questions about what we can know and how we can know it.
        
        ## Central Epistemological Questions
        
        1. **What is knowledge?** How does knowledge differ from mere opinion or belief?
        2. **What are the sources of knowledge?** Do we learn through experience, reason, or both?
        3. **What are the limits of knowledge?** Are there things we cannot know?
        4. **How do we justify our beliefs?** What makes a belief reasonable to hold?
        
        ## Classical Definition of Knowledge
        
        **Knowledge = Justified True Belief**
        
        For something to count as knowledge, it must be:
        - **Believed** (you must accept it as true)
        - **True** (it must actually be the case)
        - **Justified** (you must have good reasons for believing it)
        
        ## Sources of Knowledge
        
        **Rationalism**: Emphasizes reason and logic as primary sources
        - Knowledge comes through thinking and logical analysis
        - Mathematical truths are paradigm examples
        - Associated with philosophers like Plato and Descartes
        
        **Empiricism**: Emphasizes sensory experience as primary source
        - Knowledge comes through observation and experiment
        - Scientific knowledge is the paradigm
        - Associated with philosophers like Aristotle and Hume
        
        ## Types of Knowledge
        
        **A Priori Knowledge**: Known independently of experience
        - Mathematical truths (2+2=4)
        - Logical principles (law of non-contradiction)
        
        **A Posteriori Knowledge**: Known through experience
        - Scientific facts about the world
        - Historical events
        
        ## Skeptical Challenges
        
        **Skepticism** questions whether knowledge is possible:
        - How do we know our senses are reliable?
        - Could we be systematically deceived about reality?
        - What if our reasoning abilities are flawed?
        
        ## The Problem of the Criterion
        
        To know something, we need criteria for truth. But to establish criteria for truth, we need to know what truth is. This creates a circular problem that epistemologists must address.
        """)
        
        with st.expander("💡 Thought Experiment"):
            st.markdown("""
            **The Gettier Problem:**
            
            Smith believes Jones will get the job and Jones has 10 coins in his pocket. So Smith believes "The person who gets the job has 10 coins." 
            
            Unknown to Smith, he actually gets the job himself, and he also happens to have 10 coins in his pocket.
            
            Smith's belief is true and justified, but is it knowledge? This challenge led philosophers to reconsider the classical definition of knowledge.
            """)
    
    elif module == "Module 4: Pre-Socratic Philosophers":
        st.subheader("The Pre-Socratic Revolution")
        
        st.markdown("""
        ## The Philosophical Revolution
        
        The **Pre-Socratic philosophers** (6th-5th centuries BCE) began the first systematic attempt to understand the natural world through reason rather than mythology. This marked the birth of both philosophy and science.
        
        ## Thales (c. 624-546 BCE)
        
        **Revolutionary Insight**: Natural phenomena have natural explanations
        
        **Key Ideas:**
        - Water is the fundamental substance from which all things arise
        - Earthquakes are caused by water movements, not angry gods
        - Natural events can be predicted through observation and reasoning
        
        **Historical Significance**: First to seek rational rather than supernatural explanations
        
        ## Heraclitus (c. 535-475 BCE)
        
        **Central Doctrine**: "Everything flows" - reality is constant change
        
        **Famous Sayings:**
        - "You cannot step into the same river twice"
        - "The way up and down are one and the same"
        - "Opposition is necessary for harmony"
        
        **Key Insight**: Apparent stability emerges from underlying change and conflict
        
        ## Parmenides (c. 515-450 BCE)
        
        **Radical Claim**: Change is an illusion - reality is eternal and unchanging
        
        **The Way of Truth**:
        - What exists must be eternal, indivisible, and unchanging
        - Coming-to-be and passing-away are impossible
        - Sensory experience deceives us about reality's true nature
        
        **Method**: Pure logical reasoning reveals truth about reality
        
        ## Zeno of Elea (c. 490-430 BCE)
        
        **Purpose**: Defend Parmenides by showing the absurdity of motion and change
        
        **Famous Paradoxes:**
        
        **Achilles and the Tortoise**: Achilles can never catch a tortoise with a head start because he must always first reach where the tortoise was, by which time it has moved further ahead.
        
        **The Arrow**: At any instant, a moving arrow occupies a space equal to itself and is therefore at rest. If it's at rest at every instant, how can it move?
        
        **Historical Impact**: These paradoxes forced philosophers to think more carefully about space, time, and infinity.
        
        ## The Fundamental Debate
        
        **Heraclitus vs. Parmenides** represents a fundamental tension in philosophy:
        - Should we trust sensory experience (Heraclitus) or pure reason (Parmenides)?
        - Is reality fundamentally about change or permanence?
        - How do we reconcile the apparent conflict between experience and logic?
        
        This debate continues to influence philosophy, science, and mathematics today.
        """)
        
        with st.expander("💡 Critical Analysis"):
            st.markdown("""
            **Consider these questions:**
            
            1. **Thales's Method**: Was Thales right to seek natural explanations? What are the advantages and limitations of this approach?
            
            2. **Heraclitus vs. Parmenides**: Who do you think was closer to the truth? Can their views be reconciled?
            
            3. **Zeno's Paradoxes**: How might we resolve the paradox of Achilles and the tortoise? What does this tell us about the relationship between mathematics and reality?
            """)
    
    elif module == "Module 5: Knowledge vs. Opinion":
        st.subheader("Distinguishing Knowledge from Opinion")
        
        st.markdown("""
        ## The Fundamental Distinction
        
        One of philosophy's most important tasks is distinguishing between what we actually **know** and what we merely **believe** or **think we know**.
        
        ## Characteristics of Knowledge
        
        **Knowledge requires:**
        1. **Truth**: The belief must correspond to reality
        2. **Belief**: You must accept it as true
        3. **Justification**: You must have good reasons for believing it
        4. **Reliability**: The method of acquiring it must be dependable
        
        ## Characteristics of Opinion
        
        **Opinion typically involves:**
        - Personal preference or judgment
        - Cultural or social influence
        - Limited evidence or justification
        - Subjective rather than objective criteria
        
        ## The Spectrum of Certainty
        
        **Absolute Certainty**: Mathematical and logical truths (2+2=4)
        
        **High Probability**: Well-established scientific facts
        
        **Reasonable Belief**: Conclusions based on good evidence
        
        **Opinion**: Judgments based on limited information
        
        **Speculation**: Guesses with little supporting evidence
        
        ## Sources of Error
        
        **Why we might mistake opinion for knowledge:**
        
        1. **Confirmation Bias**: Seeking information that confirms our existing beliefs
        2. **Authority Bias**: Accepting claims because of who made them
        3. **Cultural Assumptions**: Mistaking local customs for universal truths
        4. **Emotional Attachment**: Wanting something to be true
        
        ## Tests for Knowledge Claims
        
        **Ask yourself:**
        - What evidence supports this claim?
        - Could this be explained differently?
        - What would count as evidence against it?
        - Are my sources reliable and unbiased?
        - Am I being influenced by emotion or desire?
        
        ## The Socratic Method
        
        **Socrates' approach to testing knowledge:**
        1. Ask probing questions about basic assumptions
        2. Reveal contradictions in our beliefs
        3. Admit ignorance when evidence is insufficient
        4. Continue searching for better understanding
        
        ## Practical Applications
        
        **In daily life, distinguish between:**
        - Facts that can be verified vs. personal preferences
        - Expert consensus vs. popular opinion  
        - Evidence-based conclusions vs. wishful thinking
        - Logical reasoning vs. emotional reactions
        """)
        
        with st.expander("💡 Self-Assessment"):
            st.markdown("""
            **Evaluate your own beliefs:**
            
            Think of something you're confident you "know." Apply these tests:
            
            1. **Evidence Test**: What specific evidence supports this belief?
            2. **Alternative Test**: What other explanations are possible?
            3. **Source Test**: Where did this belief come from? Is the source reliable?
            4. **Bias Test**: Might you want this to be true for personal reasons?
            
            This process helps distinguish genuine knowledge from strongly held opinions.
            """)
    
    elif module == "Module 6: Eastern Philosophy - The Upanishads":
        st.subheader("Eastern Philosophy: The Upanishads")
        
        st.markdown("""
        ## The Upanishads: Ancient Wisdom Literature
        
        The **Upanishads** (800-200 BCE) are ancient Indian philosophical texts that explore the nature of ultimate reality and the self. They represent one of humanity's earliest systematic philosophical investigations.
        
        ## Core Philosophical Concepts
        
        **Brahman**: The ultimate, unchanging reality underlying all existence
        - Beyond all qualities and descriptions
        - The source and ground of everything that exists
        - Not a personal god, but pure being itself
        
        **Atman**: The true self or soul within each individual
        - Not the body, mind, or personality
        - The eternal, unchanging essence of consciousness
        - The witness of all experience
        
        ## The Central Teaching: "Tat Tvam Asi"
        
        **"That Art Thou" (Tat tvam asi)** - The most famous teaching from the Chandogya Upanishad
        
        **Meaning**: Your true self (Atman) is identical with ultimate reality (Brahman)
        
        **Implication**: The individual soul and universal consciousness are one and the same
        
        ## The Teaching Story
        
        A father (Uddalaka) instructs his son (Svetaketu):
        
        *"Place this salt in water and return to me in the morning. Where is the salt? It has dissolved, but taste the water - everywhere it is salty. So too, dear son, the eternal essence pervades all existence. That reality is the true Self, and That Art Thou, Svetaketu."*
        
        ## Philosophical Implications
        
        **Metaphysics**: Reality is fundamentally one, not many
        - Apparent diversity is illusion (Maya)
        - Underlying unity connects all existence
        
        **Epistemology**: True knowledge is self-knowledge
        - External learning cannot reveal ultimate truth
        - Direct insight, not reasoning, leads to wisdom
        
        **Ethics**: Recognizing unity dissolves ego and selfishness
        - If all is one, harming others harms oneself
        - Compassion flows naturally from understanding
        
        ## Comparison with Western Philosophy
        
        **Similarities to Western thought:**
        - Parmenides: Reality is One and unchanging
        - Plato: Appearances vs. deeper reality
        - Plotinus: The One as source of all being
        
        **Differences from Western thought:**
        - Emphasizes direct experience over logical argument
        - Focuses on liberation from suffering, not just understanding
        - Sees rational thinking as ultimately limited
        
        ## The Method of Inquiry
        
        **"Neti, neti"** ("Not this, not this")
        - Systematic negation of everything that is not the Self
        - By eliminating what you are not, discover what you are
        - Similar to Socratic method of questioning assumptions
        
        ## Contemporary Relevance
        
        Modern physicists and philosophers have noted parallels between Upanishadic thought and:
        - Quantum mechanics (the observer-observed relationship)
        - Systems theory (interconnectedness of all phenomena)
        - Consciousness studies (the nature of subjective experience)
        """)
        
        with st.expander("💡 Philosophical Reflection"):
            st.markdown("""
            **Consider these questions:**
            
            1. **Identity**: What do you consider your "true self"? Is it your body, mind, memories, or something else?
            
            2. **Unity vs. Multiplicity**: Do you see reality as fundamentally one or many? What evidence supports each view?
            
            3. **Knowledge**: Can some truths only be known through direct experience rather than reasoning? What might be examples?
            
            4. **East meets West**: How might we combine the Upanishadic emphasis on unity with the Western emphasis on analysis and argument?
            """)

elif page == "🎯 Interactive Quiz":
    st.header("🎯 Test Your Understanding")
    
    show_score()
    
    if st.session_state.current < len(st.session_state.questions):
        show_question()
    else:
        st.balloons()
        st.success(f"🎉 **Quiz Complete!** Final Score: {st.session_state.score} XP")
        
        # Performance analysis
        total_possible = len(st.session_state.questions) * 10
        percentage = (st.session_state.score / total_possible) * 100
        
        if percentage >= 90:
            st.success("🏆 **Philosophy Master!** You've mastered the fundamentals of philosophical thinking.")
        elif percentage >= 80:
            st.info("🎓 **Advanced Understanding** - You have a solid grasp of core concepts!")
        elif percentage >= 70:
            st.warning("📚 **Good Progress** - Review the learning modules for deeper understanding.")
        else:
            st.error("🔄 **Keep Learning** - Spend more time with the learning modules before retaking.")
        
        restart_quiz()

elif page == "📊 Visualizations":
    create_visualizations()

elif page == "📚 Reference Guide":
    st.header("📚 Quick Reference Guide")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Key Terms", "Philosophers", "Arguments", "Study Tips"])
    
    with tab1:
        st.subheader("Essential Philosophical Terms")
        
        terms = {
            "Philosophy": "The systematic examination of fundamental questions about reality, knowledge, values, and existence",
            "Epistemology": "The branch of philosophy that studies the nature, sources, and limits of knowledge",
            "Metaphysics": "The branch of philosophy that examines the nature of reality and existence",
            "Logic": "The study of valid reasoning and argument structure",
            "Claim": "A statement that can be either true or false",
            "Argument": "A set of premises offered in support of a conclusion",
            "Premise": "A statement that provides evidence or support for a conclusion",
            "Conclusion": "The statement that premises are meant to support",
            "Valid": "An argument where the conclusion follows logically from the premises",
            "Sound": "A valid argument with true premises",
            "Vague": "Using words that are not precise or whose boundaries are unclear",
            "Ambiguous": "Using words that can have several possible meanings",
            "A Priori": "Knowledge that can be known independently of experience",
            "A Posteriori": "Knowledge that requires experience to be known",
            "Rationalism": "The view that reason is the primary source of knowledge",
            "Empiricism": "The view that sensory experience is the primary source of knowledge",
            "Skepticism": "The view that questions whether certain or any knowledge is possible",
            "Brahman": "In the Upanishads, the ultimate reality underlying all existence",
            "Atman": "In the Upanishads, the true self or soul within each individual"
        }
        
        for term, definition in terms.items():
            with st.expander(f"**{term}**"):
                st.write(definition)
    
    with tab2:
        st.subheader("Key Philosophers")
        
        philosophers = {
            "Thales (c. 624-546 BCE)": {
                "Key Idea": "Water is the fundamental substance; natural phenomena have natural explanations",
                "Significance": "First Western philosopher to seek rational rather than mythological explanations",
                "Quote": "'All things are full of gods' (meaning natural forces, not supernatural beings)"
            },
            "Heraclitus (c. 535-475 BCE)": {
                "Key Idea": "Everything flows - reality is constant change and flux",
                "Significance": "Emphasized the role of change and opposition in understanding reality",
                "Quote": "You cannot step into the same river twice"
            },
            "Parmenides (c. 515-450 BCE)": {
                "Key Idea": "Change is illusion - reality is eternal, unchanging Being",
                "Significance": "Used pure reason to argue against the evidence of the senses",
                "Quote": "What is, is; what is not, is not"
            },
            "Zeno of Elea (c. 490-430 BCE)": {
                "Key Idea": "Motion and change lead to logical contradictions",
                "Significance": "Created paradoxes that challenged assumptions about space and time",
                "Quote": "The moving arrow is at rest"
            },
            "Socrates (470-399 BCE)": {
                "Key Idea": "The unexamined life is not worth living; true knowledge begins with admitting ignorance",
                "Significance": "Developed the method of systematic questioning to test beliefs",
                "Quote": "I know that I know nothing"
            }
        }
        
        for name, info in philosophers.items():
            with st.expander(f"**{name}**"):
                st.write(f"**Key Idea**: {info['Key Idea']}")
                st.write(f"**Significance**: {info['Significance']}")
                st.write(f"**Famous Quote**: '{info['Quote']}'")
    
    with tab3:
        st.subheader("Argument Analysis Guide")
        
        st.markdown("""
        ## Steps for Analyzing Arguments
        
        1. **Identify the Conclusion**: What is the main point being argued?
        2. **Find the Premises**: What evidence or reasons support the conclusion?
        3. **Check for Hidden Assumptions**: What unstated beliefs are required?
        4. **Evaluate Validity**: Does the conclusion follow logically from the premises?
        5. **Assess Truth**: Are the premises actually true?
        
        ## Common Argument Forms
        
        **Deductive (All A are B, X is A, therefore X is B)**
        - If premises are true, conclusion must be true
        - Example: All humans are mortal, Socrates is human, therefore Socrates is mortal
        
        **Inductive (Pattern-based reasoning)**
        - Premises make conclusion probable, not certain
        - Example: The sun has risen every day in the past, therefore it will rise tomorrow
        
        **Abductive (Inference to best explanation)**
        - Conclusion explains the evidence better than alternatives
        - Example: The ground is wet, therefore it probably rained
        
        ## Argument Errors to Avoid
        
        - **Ad Hominem**: Attacking the person instead of their argument
        - **Straw Man**: Misrepresenting someone's position to make it easier to attack
        - **False Dichotomy**: Presenting only two options when more exist
        - **Circular Reasoning**: Using the conclusion to support itself
        - **Appeal to Authority**: Accepting a claim just because an authority said it
        """)
    
    with tab4:
        st.subheader("Study Tips & Strategies")
        
        st.markdown("""
        ## Effective Philosophy Study Methods
        
        **Active Reading:**
        - Ask questions as you read: "What is the main claim? What evidence supports it?"
        - Summarize key points in your own words
        - Look up unfamiliar terms immediately
        
        **Critical Analysis:**
        - Don't just memorize - understand the reasoning
        - Practice identifying premises and conclusions
        - Consider alternative viewpoints and counterarguments
        
        **Discussion & Debate:**
        - Explain concepts to others to test your understanding
        - Engage in respectful philosophical discussions
        - Be willing to change your mind when presented with better arguments
        
        **Writing Practice:**
        - Write out arguments in standard form
        - Practice defining vague or ambiguous terms
        - Construct your own philosophical arguments
        
        ## Common Study Mistakes
        
        **Avoid these pitfalls:**
        - Thinking philosophy is just about opinions (it's about reasoned arguments)
        - Memorizing without understanding the logic
        - Dismissing ideas without considering them carefully
        - Confusing difficult with impossible to understand
        
        ## Quiz Preparation
        
        **Before taking the quiz:**
        1. Review all learning modules thoroughly
        2. Practice identifying arguments and their components
        3. Make sure you can define key terms clearly
        4. Understand the historical significance of major philosophers
        5. Practice applying concepts to new examples
        
        **During the quiz:**
        - Read questions carefully - philosophy is precise
        - Eliminate obviously wrong answers first
        - Consider what concepts each question is testing
        - Don't overthink - your first careful analysis is often correct
        """)

elif page == "🔗 Resources & Links":
    st.header("🔗 Philosophy Resources & External Links")
    st.markdown("**Expand your philosophical knowledge with these curated resources**")
    
    # Create tabs for different resource categories
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 Academic Resources", "🛠️ Logic Tools", "🎬 Videos & Podcasts", "📖 Classic Texts", "💻 Practice Platforms"])
    
    with tab1:
        st.subheader("📚 Academic Databases & Encyclopedias")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎓 Primary Academic Sources")
            
            if st.button("📖 Stanford Encyclopedia of Philosophy", use_container_width=True):
                st.markdown("**[Open Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)**")
                st.success("The most authoritative philosophy reference - peer-reviewed articles by experts on every philosophical topic.")
                st.info("**Recommended articles**: Epistemology, Knowledge Analysis, Ancient Philosophy, Rationalism vs Empiricism")
            
            if st.button("📚 Internet Encyclopedia of Philosophy", use_container_width=True):
                st.markdown("**[Open Internet Encyclopedia of Philosophy](https://iep.utm.edu/)**")
                st.success("Comprehensive philosophy articles with more accessible language than SEP.")
                st.info("**Recommended sections**: Epistemology, Pre-Socratic Philosophy, Indian Philosophy")
            
            if st.button("🔍 PhilPapers Database", use_container_width=True):
                st.markdown("**[Search PhilPapers.org](https://philpapers.org/)**")
                st.success("Search over 2.9 million philosophy papers and books.")
                st.info("**Try searching**: 'epistemology basics', 'pre-socratic philosophy', 'knowledge definition'")
        
        with col2:
            st.markdown("### 🏛️ University Resources")
            
            if st.button("🎓 MIT OpenCourseWare Philosophy", use_container_width=True):
                st.markdown("**[Access MIT Philosophy Courses](https://ocw.mit.edu/courses/linguistics-and-philosophy/)**")
                st.success("Free access to actual MIT philosophy course materials and lectures.")
                st.info("**Recommended**: Introduction to Philosophy, Epistemology, Logic")
            
            if st.button("📺 Yale Open Courses", use_container_width=True):
                st.markdown("**[Yale Philosophy Lectures](https://oyc.yale.edu/philosophy)**")
                st.success("Full video lectures from Yale philosophy professors.")
                st.info("**Start with**: Introduction to Philosophy (PHIL 181)")
            
            if st.button("📊 Philosophy Compass", use_container_width=True):
                st.markdown("**[Philosophy Compass](https://onlinelibrary.wiley.com/journal/17479991)**")
                st.success("Short, accessible surveys of philosophical topics.")
                st.info("**Note**: May require library access through your institution")
    
    with tab2:
        st.subheader("🛠️ Interactive Logic & Reasoning Tools")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ⚡ Logic Practice Tools")
            
            if st.button("🔬 MIT Logitext", use_container_width=True):
                st.markdown("**[Open MIT Logitext](https://logitext.mit.edu/main)**")
                st.success("Interactive logic tool for practicing propositional and predicate logic.")
                st.code("Try this: (P ∧ Q) → R")
                st.info("Perfect for understanding logical operators and argument forms!")
            
            if st.button("📊 Stanford Truth Table Tool", use_container_width=True):
                st.markdown("**[Stanford Truth Table Generator](https://web.stanford.edu/class/cs103/tools/truth-table-tool/)**")
                st.success("Generate truth tables for any logical expression.")
                st.info("**Example**: Input 'P ∧ Q' to see how conjunction works")
            
            if st.button("🎯 Logic & Proofs Platform", use_container_width=True):
                st.markdown("**[Open Logic & Proofs](https://logicinaction.org/)**")
                st.success("Interactive exercises for learning formal logic step by step.")
        
        with col2:
            st.markdown("### 📈 Argument Analysis Tools")
            
            if st.button("🗺️ Rationale Online", use_container_width=True):
                st.markdown("**[Rationale Argument Mapping](https://www.rationaleonline.com/)**")
                st.success("Visual argument analysis - map premises and conclusions.")
                st.info("Great for understanding the structure of complex philosophical arguments")
            
            if st.button("🔍 Argument Clinic", use_container_width=True):
                st.markdown("**[The Argument Clinic](https://www.criticalthinking.org.uk/)**")
                st.success("Interactive critical thinking exercises and argument evaluation.")
            
            if st.button("📝 Critical Thinking Web", use_container_width=True):
                st.markdown("**[Critical Thinking Web (UBC)](https://philosophy.hku.hk/think/)**")
                st.success("University of Hong Kong's comprehensive critical thinking tutorials.")
    
    with tab3:
        st.subheader("🎬 Educational Videos & Podcasts")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎧 Philosophy Podcasts")
            
            if st.button("🎭 Philosophy Bites", use_container_width=True):
                st.markdown("**[Philosophy Bites Podcast](https://www.philosophybites.com/)**")
                st.success("15-minute interviews with leading philosophers on key topics.")
                st.info("**Start with**: 'What is Knowledge?' and 'The Importance of Philosophy'")
            
            if st.button("🧠 The History of Philosophy", use_container_width=True):
                st.markdown("**[History of Philosophy Podcast](https://historyofphilosophy.net/)**")
                st.success("Comprehensive journey through philosophical history without any gaps.")
                st.info("**Episodes 1-20**: Perfect introduction to Pre-Socratic philosophers")
            
            if st.button("🤔 Philosophy Talk", use_container_width=True):
                st.markdown("**[Philosophy Talk](https://www.philosophytalk.org/)**")
                st.success("Stanford's radio show making philosophy accessible to everyone.")
        
        with col2:
            st.markdown("### 📺 Educational Videos")
            
            if st.button("🎓 Crash Course Philosophy", use_container_width=True):
                st.markdown("**[Crash Course Philosophy Playlist](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNgK6MZucdYldNkMybYIHKR)**")
                st.success("Engaging 10-minute videos covering major philosophical concepts.")
                st.info("**Episode 8**: 'Knowledge & Skepticism' directly relates to our epistemology module")
            
            if st.button("🎬 TED-Ed Philosophy", use_container_width=True):
                st.markdown("**[TED-Ed Philosophy Videos](https://www.youtube.com/results?search_query=TED-Ed+philosophy)**")
                st.success("High-quality animated explanations of philosophical concepts.")
                st.info("**Recommended**: 'Plato's Allegory of the Cave' and 'What is Consciousness?'")
            
            if st.button("🏛️ Academy of Ideas", use_container_width=True):
                st.markdown("**[Academy of Ideas](https://www.youtube.com/c/AcademyofIdeas)**")
                st.success("In-depth explorations of philosophical and psychological concepts.")
    
    with tab4:
        st.subheader("📖 Classical Philosophy Texts")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📜 Primary Sources")
            
            if st.button("📚 Project Gutenberg Philosophy", use_container_width=True):
                st.markdown("**[Free Classical Philosophy Texts](https://www.gutenberg.org/ebooks/subject/11)**")
                st.success("Free access to classic philosophical works in the public domain.")
                st.info("**Includes**: Plato's dialogues, Aristotle's works, and more")
            
            if st.button("🏛️ Perseus Digital Library", use_container_width=True):
                st.markdown("**[Perseus Ancient Philosophy](http://www.perseus.tufts.edu/)**")
                st.success("Original Greek and Latin texts with English translations.")
                st.info("**Perfect for**: Reading Pre-Socratic fragments in context")
            
            if st.button("📖 Sacred Texts - Philosophy", use_container_width=True):
                st.markdown("**[Sacred-Texts Philosophy Section](https://www.sacred-texts.com/phi/)**")
                st.success("Including the Upanishads and other Eastern philosophical texts.")
                st.info("**Recommended**: The Principal Upanishads for 'That art thou' context")
        
        with col2:
            st.markdown("### 🔖 Study Guides")
            
            if st.button("📝 SparkNotes Philosophy", use_container_width=True):
                st.markdown("**[SparkNotes Philosophy Study Guides](https://www.sparknotes.com/philosophy/)**")
                st.success("Accessible summaries of major philosophical works and thinkers.")
                st.info("**Helpful for**: Quick reviews of philosopher's main ideas")
            
            if st.button("📊 Philosophy Study Guides", use_container_width=True):
                st.markdown("**[Various University Study Guides](https://www.google.com/search?q=philosophy+study+guides+university)**")
                st.success("Many universities provide free study guides for philosophy courses.")
            
            if st.button("🎯 CliffsNotes Philosophy", use_container_width=True):
                st.markdown("**[CliffsNotes Philosophy](https://www.cliffsnotes.com/study-guides/philosophy)**")
                st.success("Structured study guides for major philosophical topics.")
    
    with tab5:
        st.subheader("💻 Interactive Practice Platforms")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎮 Philosophy Games & Quizzes")
            
            if st.button("🧩 Philosophical Health Check", use_container_width=True):
                st.markdown("**[Philosophy Health Check](https://www.philosophyexperiments.com/)**")
                st.success("Test the consistency of your philosophical beliefs.")
                st.info("Interactive thought experiments that challenge your reasoning")
            
            if st.button("🎯 Philosophy Quiz Sites", use_container_width=True):
                st.markdown("**[Various Philosophy Quizzes](https://www.sporcle.com/games/subcategory/philosophy)**")
                st.success("Test your knowledge of philosophers, concepts, and arguments.")
            
            if st.button("🤔 Thought Experiment Hub", use_container_width=True):
                st.markdown("**[Thought Experiments](https://www.google.com/search?q=interactive+philosophy+thought+experiments)**")
                st.success("Explore classic philosophical puzzles interactively.")
        
        with col2:
            st.markdown("### 📚 Study Communities")
            
            if st.button("💬 Reddit Philosophy", use_container_width=True):
                st.markdown("**[r/philosophy](https://www.reddit.com/r/philosophy/)**")
                st.success("Active discussions about philosophical topics.")
                st.warning("**Remember**: Always verify information with academic sources")
            
            if st.button("🎓 Philosophy Forums", use_container_width=True):
                st.markdown("**[Philosophy Forums](https://www.philosophyforums.com/)**")
                st.success("Discuss philosophical questions with other students and enthusiasts.")
            
            if st.button("📱 Philosophy Apps", use_container_width=True):
                st.markdown("**[Search App Stores](https://www.google.com/search?q=philosophy+apps+education)**")
                st.success("Many mobile apps offer philosophy quizzes and concept reviews.")
    
    st.markdown("---")
    st.subheader("🎯 How to Use These Resources Effectively")
    
    tip_cols = st.columns(3)
    with tip_cols[0]:
        st.markdown("""
        **📖 For Deeper Learning**
        - Use Stanford Encyclopedia for authoritative information
        - Watch Crash Course videos for visual explanations
        - Listen to Philosophy Bites for expert perspectives
        """)
    
    with tip_cols[1]:
        st.markdown("""
        **🛠️ For Practice**
        - Use logic tools to understand argument structure
        - Try interactive exercises to test comprehension
        - Join forums for discussion and debate
        """)
    
    with tip_cols[2]:
        st.markdown("""
        **📚 For Research**
        - Start with our learning modules for foundation
        - Use PhilPapers for current scholarship
        - Verify information across multiple sources
        """)
    
    st.info("💡 **Study Tip**: Always return to our learning modules to connect external resources with course concepts!")

elif page == "🤖 AI Philosophy Tutor":
    st.header("🤖 AI Philosophy Tutor")
    st.markdown("**Get personalized help with philosophical concepts and questions**")
    
    try:
        import anthropic
        
        # Initialize Anthropic client
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        
        # Suggested questions
        st.subheader("💡 Quick Help Topics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Concepts & Definitions:**")
            if st.button("What's the difference between knowledge and opinion?", use_container_width=True):
                st.session_state.current_question = "Explain the difference between knowledge and opinion, and how philosophers distinguish between them."
            
            if st.button("How do I identify premises and conclusions?", use_container_width=True):
                st.session_state.current_question = "How do I identify the premises and conclusion in a philosophical argument? Can you give me some examples?"
            
            if st.button("What made Thales revolutionary?", use_container_width=True):
                st.session_state.current_question = "Why was Thales considered revolutionary in the history of philosophy? What made his approach different?"
        
        with col2:
            st.markdown("**Problem-Solving:**")
            if st.button("Help me understand Zeno's paradoxes", use_container_width=True):
                st.session_state.current_question = "Can you explain Zeno's paradoxes and why they were philosophically important? How might we resolve them?"
            
            if st.button("Explain rationalism vs empiricism", use_container_width=True):
                st.session_state.current_question = "What's the difference between rationalism and empiricism in epistemology? Can you give examples of each?"
            
            if st.button("What does 'That art thou' mean?", use_container_width=True):
                st.session_state.current_question = "Explain the meaning and significance of 'That art thou' from the Upanishads. What philosophical insight does it convey?"
        
        # Initialize chat history
        if 'tutor_chat_history' not in st.session_state:
            st.session_state.tutor_chat_history = []
        
        # Handle suggested questions
        if 'current_question' in st.session_state:
            st.session_state.user_input = st.session_state.current_question
            del st.session_state.current_question
        
        # Chat interface
        st.subheader("💬 Ask Your Philosophy Tutor")
        
        # Display chat history
        for i, (question, answer) in enumerate(st.session_state.tutor_chat_history):
            with st.container():
                st.markdown(f"**🧠 You:** {question}")
                st.markdown(f"**🤖 Tutor:** {answer}")
                st.markdown("---")
        
        # User input
        user_question = st.text_area(
            "Ask your question:",
            value=st.session_state.get('user_input', ''),
            height=100,
            placeholder="e.g., I'm confused about the difference between Heraclitus and Parmenides..."
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            ask_button = st.button("📚 Ask Tutor", type="primary")
        with col2:
            if st.button("🗑️ Clear Chat"):
                st.session_state.tutor_chat_history = []
                st.rerun()
        
        if ask_button and user_question.strip():
            with st.spinner("🤔 Thinking about your question..."):
                try:
                    # Create tutor prompt
                    system_prompt = """You are a philosophy tutor helping students learn the fundamentals of philosophy and epistemology. Your role is to:

1. Explain concepts clearly and accurately
2. Help students understand rather than just giving answers
3. Use Socratic questioning when appropriate
4. Provide examples to illustrate abstract concepts
5. Connect ideas to show how philosophical concepts relate
6. Encourage critical thinking

The course covers:
- Nature of philosophy and its methods
- Critical thinking and argument analysis
- Epistemology (theory of knowledge)
- Pre-Socratic philosophers (Thales, Heraclitus, Parmenides, Zeno)
- Knowledge vs opinion
- Eastern philosophy (Upanishads)
- Philosophical claims, vagueness, and ambiguity

Be encouraging and patient, but also challenge students to think deeply. When they ask for help understanding a concept, don't just define it - help them see why it matters and how it connects to other ideas."""

                    # Get response from Claude
                    message = client.messages.create(
                        model="claude-3-haiku-20240307",
                        max_tokens=1000,
                        temperature=0.7,
                        system=system_prompt,
                        messages=[{
                            "role": "user", 
                            "content": user_question
                        }]
                    )
                    
                    response = message.content[0].text
                    
                    # Add to chat history
                    st.session_state.tutor_chat_history.append((user_question, response))
                    
                    # Clear input
                    st.session_state.user_input = ""
                    
                    # Rerun to show new response
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"Error getting response: {str(e)}")
                    st.info("Please check your API key and try again.")
    
    except ImportError:
        st.error("📦 Missing required library. Please install: `pip install anthropic`")
    
    # Study tips
    st.markdown("---")
    st.subheader("💡 How to Use Your AI Tutor Effectively")
    
    tip_cols = st.columns(3)
    with tip_cols[0]:
        st.markdown("""
        **🎯 Be Specific**
        - Ask about particular concepts you're struggling with
        - Provide context about what you do and don't understand
        - Give examples when possible
        """)
    
    with tip_cols[1]:
        st.markdown("""
        **🤔 Engage Actively**
        - Ask follow-up questions
        - Challenge ideas respectfully
        - Connect new concepts to what you already know
        """)
    
    with tip_cols[2]:
        st.markdown("""
        **📚 Apply Learning**
        - Use the tutor to clarify learning module content
        - Get help understanding quiz questions
        - Practice explaining concepts in your own words
        """)

# Footer
st.markdown("---")
st.markdown("**Built for philosophical learning | Philosophy Foundations & Epistemology CognitiveCloud.ai**")
st.caption("© 2024 Interactive Philosophy Education Platform")
