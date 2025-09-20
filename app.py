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
