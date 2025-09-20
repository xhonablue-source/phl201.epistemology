import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# SECURE API KEY HANDLING
ANTHROPIC_API_KEY = st.secrets["ANTHROPIC_API_KEY"]

st.set_page_config(page_title="PHL201 Epistemology - CognitiveCloud.ai", layout="wide", initial_sidebar_state="expanded")

# Epistemology-focused questions
questions = [
    ("What is epistemology?", 
     ["The study of being", "The study of knowledge and truth", "The study of ethics", "The study of logic"], 
     "The study of knowledge and truth"),
    
    ("What is a philosophical claim?", 
     ["An emotion", "A declarative sentence that can be true or false", "A question", "A belief"], 
     "A declarative sentence that can be true or false"),
    
    ("Theoretical thinking holds that:", 
     ["Multiple views can be true", "If one view is correct, different views must be incorrect", "All opinions are equal", "Truth is relative"], 
     "If one view is correct, different views must be incorrect"),
    
    ("A vague claim:", 
     ["Is about abstracts", "Uses imprecise words with unclear boundaries", "Is controversial", "Is complex"], 
     "Uses imprecise words with unclear boundaries"),
    
    ("An ambiguous claim:", 
     ["Is false", "Can have several possible meanings", "Is simple", "Needs expertise"], 
     "Can have several possible meanings"),
    
    ("To avoid vagueness:", 
     ["Use technical terms", "Define terms through examples, synonyms, or explanations", "Avoid topics", "Discuss facts only"], 
     "Define terms through examples, synonyms, or explanations"),
    
    ("Philosophical arguments differ from opinions because they:", 
     ["Are always true", "Provide premises to support conclusions", "Are popular", "Are easy"], 
     "Provide premises to support conclusions"),
    
    ("The classical definition of knowledge is:", 
     ["True belief", "Justified true belief", "Certain belief", "Popular belief"], 
     "Justified true belief"),
    
    ("Rationalism emphasizes:", 
     ["Experience only", "Reason and logic", "Authority", "Intuition only"], 
     "Reason and logic"),
    
    ("Empiricism emphasizes:", 
     ["Reason only", "Sensory experience and observation", "Revelation", "Mathematical proof"], 
     "Sensory experience and observation"),
    
    ("A priori knowledge:", 
     ["Requires experience", "Can be known independently of experience", "Comes from authorities", "Changes over time"], 
     "Can be known independently of experience"),
    
    ("The Gettier problem challenges:", 
     ["Truth existence", "The classical definition of knowledge as justified true belief", "Belief possibility", "Justification need"], 
     "The classical definition of knowledge as justified true belief"),
    
    ("Anarchic thinking:", 
     ["Studies different subjects", "Accepts multiple valid perspectives while theoretical seeks one correct view", "Uses different methods", "Is ancient"], 
     "Accepts multiple valid perspectives while theoretical seeks one correct view"),
    
    ("Skepticism questions:", 
     ["Religious beliefs only", "Whether knowledge is possible", "Scientific claims only", "Arguments only"], 
     "Whether knowledge is possible"),
    
    ("Foundationalism claims:", 
     ["All beliefs are equal", "Some beliefs are basic and need no justification from others", "No beliefs can be justified", "Only empirical beliefs count"], 
     "Some beliefs are basic and need no justification from others"),
    
    ("Coherentism argues:", 
     ["Only foundations matter", "Beliefs are justified by fitting coherently together", "No justification possible", "Only experience matters"], 
     "Beliefs are justified by fitting coherently together"),
    
    ("Reliabilism judges knowledge based on:", 
     ["Popular consensus", "Whether the belief-forming process is reliable", "Authority endorsement", "Emotional certainty"], 
     "Whether the belief-forming process is reliable"),
    
    ("The problem of the criterion refers to:", 
     ["Measuring difficulty", "The circular challenge of needing criteria for truth to establish criteria", "Education cost", "Learning time"], 
     "The circular challenge of needing criteria for truth to establish criteria"),
    
    ("Philosophy differs from other fields because it:", 
     ["Studies ancient texts only", "Examines fundamental assumptions other fields take for granted", "Requires no evidence", "Focuses on practical problems only"], 
     "Examines fundamental assumptions other fields take for granted"),
    
    ("Knowledge differs from opinion because:", 
     ["Knowledge is popular", "Knowledge has rational justification and corresponds to reality", "Knowledge is easier", "Knowledge never changes"], 
     "Knowledge has rational justification and corresponds to reality")
]

# Session state
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
    if st.session_state.current < len(st.session_state.questions):
        q, opts, correct = st.session_state.questions[st.session_state.current]
        
        progress = (st.session_state.current + 1) / len(st.session_state.questions)
        st.progress(progress, text=f"Question {st.session_state.current + 1} of {len(st.session_state.questions)}")
        
        st.subheader(f"Question {st.session_state.current + 1}")
        st.write(f"**{q}**")
        
        if not st.session_state.answered:
            ans = st.radio("Choose your answer:", opts, key=f"q{st.session_state.current}")
            st.session_state.selected_answer = ans
            
            if st.button("Submit Answer", type="primary"):
                if ans == correct:
                    st.session_state.feedback = ("success", "Correct! +10 XP")
                    st.session_state.score += 10
                else:
                    st.session_state.feedback = ("error", f"Incorrect. The answer is: {correct}")
                st.session_state.answered = True
                st.rerun()
        else:
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
    if st.session_state.feedback:
        typ, msg = st.session_state.feedback
        if typ == "success":
            st.success(msg)
        else:
            st.error(msg)

def show_score():
    col1, col2, col3 = st.columns(3)
    with col2:
        st.metric("Current Score", f"{st.session_state.score} XP", 
                 delta=f"{st.session_state.current} answered")

def restart_quiz():
    if st.button("Restart Assessment", type="secondary"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.feedback = None
        st.session_state.selected_answer = None
        st.session_state.answered = False
        st.rerun()

def create_visualizations():
    st.header("Epistemological Concept Visualizations")
    
    tab1, tab2 = st.tabs(["Knowledge Sources", "JTB Analysis"])
    
    with tab1:
        st.subheader("Sources of Knowledge in Epistemology")
        
        sources = ['Sensory Experience', 'Reason & Logic', 'Intuition', 'Authority', 'Testimony']
        values = [35, 30, 15, 12, 8]
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
        
        fig = go.Figure(data=[go.Pie(labels=sources, values=values, hole=.3)])
        fig.update_traces(hoverinfo="label+percent", textinfo="label+percent", 
                         textfont_size=10, marker=dict(colors=colors))
        fig.update_layout(title="Epistemological Sources of Knowledge", height=500)
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.write("**Rationalism**: Knowledge primarily through reason")
        st.write("**Empiricism**: Knowledge primarily through sensory experience")
    
    with tab2:
        st.subheader("JTB Analysis of Knowledge")
        
        fig = go.Figure()
        
        fig.add_shape(type="circle", x0=0, y0=1, x1=2, y1=3, 
                     fillcolor="rgba(255, 0, 0, 0.3)", line=dict(color="red"))
        fig.add_annotation(x=0.5, y=2.5, text="Belief", showarrow=False, font=dict(size=14))
        
        fig.add_shape(type="circle", x0=1.5, y0=1, x1=3.5, y1=3, 
                     fillcolor="rgba(0, 255, 0, 0.3)", line=dict(color="green"))
        fig.add_annotation(x=3, y=2.5, text="Truth", showarrow=False, font=dict(size=14))
        
        fig.add_shape(type="circle", x0=0.75, y0=0, x1=2.75, y1=2, 
                     fillcolor="rgba(0, 0, 255, 0.3)", line=dict(color="blue"))
        fig.add_annotation(x=1.75, y=0.5, text="Justification", showarrow=False, font=dict(size=14))
        
        fig.add_annotation(x=1.75, y=1.8, text="KNOWLEDGE", showarrow=False, 
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
        
        st.info("The Gettier Problem: Cases where someone has justified true belief but intuitively lacks knowledge")

# Main Application Layout
st.title("PHL201 Epistemology - CognitiveCloud.ai")
st.markdown("**Interactive Epistemology Learning Platform | Developed by Xavier Honablue M.Ed**")

# Sidebar
with st.sidebar:
    st.header("Course Navigation")
    page = st.radio("Choose Section:", [
        "Course Introduction", 
        "Core Modules",
        "Knowledge Assessment", 
        "Visualizations", 
        "Quick Reference",
        "Resources",
        "AI Tutor"
    ])
    
    st.markdown("---")
    st.subheader("Your Progress")
    if st.session_state.questions:
        progress_pct = (st.session_state.current / len(st.session_state.questions)) * 100
        st.metric("Assessment Progress", f"{progress_pct:.1f}%")
        st.metric("Knowledge Points", f"{st.session_state.score} XP")

# Main content
if page == "Course Introduction":
    st.header("PHL201: Introduction to Epistemology")
    st.markdown("**Developed by Xavier Honablue M.Ed | CognitiveCloud.ai**")
    
    st.write("## What is Epistemology?")
    st.write("Epistemology is the branch of philosophy that investigates the nature, sources, and limits of human knowledge.")
    
    st.write("## Core Course Themes")
    st.write("- The Nature of Knowledge: What distinguishes knowledge from belief?")
    st.write("- Sources of Knowledge: Rationalism vs. Empiricism")
    st.write("- Philosophical Reasoning: Constructing clear arguments")
    st.write("- Epistemological Problems: Skepticism, the Gettier problem")
    
    st.write("## Learning Objectives")
    st.write("1. Analyze the concept of knowledge")
    st.write("2. Evaluate different theories about knowledge sources")
    st.write("3. Construct clear philosophical arguments")
    st.write("4. Apply epistemological concepts to real-world claims")
    st.write("5. Discuss major epistemological problems")

elif page == "Core Modules":
    st.header("Core Epistemology Learning Modules")
    
    module = st.selectbox("Choose a learning module:", [
        "Module 1: What is Epistemology?",
        "Module 2: Knowledge vs. Belief", 
        "Module 3: The JTB Definition",
        "Module 4: The Gettier Problem",
        "Module 5: Rationalism vs. Empiricism"
    ])
    
    if module == "Module 1: What is Epistemology?":
        st.subheader("What is Epistemology?")
        st.write("Epistemology is the theory of knowledge. It asks fundamental questions:")
        st.write("- What is knowledge?")
        st.write("- How do we acquire knowledge?")
        st.write("- What are the limits of knowledge?")
        st.write("- How do we distinguish knowledge from belief?")
        
        with st.expander("Reflection Questions"):
            st.write("1. What's something you're confident you know?")
            st.write("2. How do you decide whether to believe new information?")
            st.write("3. Is there a difference between knowing and being certain?")
    
    elif module == "Module 2: Knowledge vs. Belief":
        st.subheader("Knowledge vs. Belief and Opinion")
        st.write("Knowledge differs from belief in important ways:")
        st.write("- Knowledge requires truth")
        st.write("- Knowledge requires justification")
        st.write("- Knowledge is not accidental")
        
        st.write("Opinion characteristics:")
        st.write("- Personal judgment")
        st.write("- Limited evidence")
        st.write("- Reasonable disagreement possible")
    
    elif module == "Module 3: The JTB Definition":
        st.subheader("The Classical Definition of Knowledge")
        st.write("For centuries, philosophers defined knowledge as Justified True Belief (JTB):")
        st.write("1. **Belief**: You must believe the proposition")
        st.write("2. **Truth**: The proposition must be true")
        st.write("3. **Justification**: You must have good reasons")
        
        st.write("Example: You know it's raining because:")
        st.write("- You believe it's raining")
        st.write("- It is actually raining")
        st.write("- You can see/hear the rain")
    
    elif module == "Module 4: The Gettier Problem":
        st.subheader("The Gettier Problem")
        st.write("In 1963, Edmund Gettier challenged the JTB definition with counterexamples.")
        
        st.write("**Gettier Case Example:**")
        st.write("Smith believes Jones will get the job and has 10 coins.")
        st.write("Smith concludes: 'The person who gets the job has 10 coins.'")
        st.write("Plot twist: Smith gets the job and also has 10 coins!")
        
        st.write("Smith has justified true belief but not knowledge - it's just lucky coincidence.")
    
    elif module == "Module 5: Rationalism vs. Empiricism":
        st.subheader("Sources of Knowledge: Rationalism vs. Empiricism")
        
        st.write("**Rationalism:**")
        st.write("- Reason is the primary source of knowledge")
        st.write("- Some knowledge is a priori (independent of experience)")
        st.write("- Mathematical truths as examples")
        st.write("- Key figures: Descartes, Plato")
        
        st.write("**Empiricism:**")
        st.write("- Experience is the primary source of knowledge")
        st.write("- Knowledge is a posteriori (requires experience)")
        st.write("- Scientific observation as paradigm")
        st.write("- Key figures: Locke, Hume")

elif page == "Knowledge Assessment":
    st.header("Test Your Epistemological Understanding")
    
    show_score()
    
    if st.session_state.current < len(st.session_state.questions):
        show_question()
    else:
        st.balloons()
        st.success(f"Assessment Complete! Final Score: {st.session_state.score} XP")
        
        total_possible = len(st.session_state.questions) * 10
        percentage = (st.session_state.score / total_possible) * 100
        
        if percentage >= 90:
            st.success("Epistemology Expert! You've mastered the theory of knowledge.")
        elif percentage >= 80:
            st.info("Strong Understanding - You grasp most key concepts!")
        elif percentage >= 70:
            st.warning("Good Foundation - Review specific modules for deeper understanding.")
        else:
            st.error("Keep Learning - Spend more time with the core modules.")
        
        restart_quiz()

elif page == "Visualizations":
    create_visualizations()

elif page == "Quick Reference":
    st.header("Epistemology Quick Reference")
    
    tab1, tab2 = st.tabs(["Key Terms", "Major Theories"])
    
    with tab1:
        st.subheader("Essential Terms")
        
        terms = {
            "Epistemology": "The study of knowledge, truth, and justification",
            "Knowledge": "Traditionally: justified true belief",
            "JTB": "Justified True Belief - the classical definition of knowledge",
            "Gettier Problem": "Cases showing JTB is insufficient for knowledge",
            "A Priori": "Knowledge independent of experience",
            "A Posteriori": "Knowledge requiring experience",
            "Rationalism": "Reason as primary source of knowledge",
            "Empiricism": "Experience as primary source of knowledge",
            "Skepticism": "Questioning whether knowledge is possible",
            "Foundationalism": "Some beliefs are basic, need no justification",
            "Coherentism": "Beliefs justified by fitting together coherently"
        }
        
        for term, definition in terms.items():
            with st.expander(f"**{term}**"):
                st.write(definition)
    
    with tab2:
        st.subheader("Major Theories")
        
        st.write("**Foundationalism**: Knowledge has basic, self-justifying beliefs")
        st.write("**Coherentism**: Beliefs are justified by coherence with other beliefs")
        st.write("**Reliabilism**: Knowledge comes from reliable processes")
        st.write("**Virtue Epistemology**: Knowledge involves intellectual virtues")

elif page == "Resources":
    st.header("Epistemology Resources")
    
    st.subheader("Academic Sources")
    st.markdown("- **[Stanford Encyclopedia: Epistemology](https://plato.stanford.edu/entries/epistemology/)**")
    st.markdown("- **[Stanford Encyclopedia: Knowledge Analysis](https://plato.stanford.edu/entries/knowledge-analysis/)**")
    st.markdown("- **[Internet Encyclopedia: Epistemology](https://iep.utm.edu/epistemo/)**")
    st.markdown("- **[The Gettier Problem](https://plato.stanford.edu/entries/knowledge-analysis/#GettProb)**")
    
    st.subheader("Educational Videos")
    st.markdown("- **[Crash Course Philosophy: Epistemology](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNgK6MZucdYldNkMybYIHKR)**")
    st.markdown("- **[Khan Academy: Philosophy](https://www.khanacademy.org/humanities/philosophy)**")
    
    st.subheader("Classic Papers")
    st.markdown("- **[Gettier: Is Justified True Belief Knowledge?](https://www.jstor.org/stable/3326922)**")
    st.markdown("- **[Goldman: What is Justified Belief?](https://www.jstor.org/stable/2025082)**")

elif page == "AI Tutor":
    st.header("Epistemology AI Tutor")
    st.write("Get personalized help with epistemological concepts")
    
    # Simplified AI interaction
    st.subheader("Common Questions")
    
    if st.button("What's the difference between knowledge and belief?"):
        st.write("**AI Response**: Knowledge typically requires three conditions that belief alone doesn't: it must be true, justified, and not accidentally true. A belief can be false, but knowledge cannot be. Additionally, knowledge requires good reasons (justification), while beliefs can be held without adequate evidence.")
    
    if st.button("Explain the Gettier problem"):
        st.write("**AI Response**: The Gettier problem shows that justified true belief isn't sufficient for knowledge. In Gettier cases, someone has a justified true belief that turns out to be true by accident or luck, disconnected from their justification. This suggests we need a fourth condition beyond belief, truth, and justification.")
    
    if st.button("Rationalism vs Empiricism?"):
        st.write("**AI Response**: Rationalists emphasize reason and logic as the primary source of knowledge, arguing some knowledge is a priori (independent of experience). Empiricists emphasize sensory experience and observation, arguing knowledge is a posteriori (requires experience). Most contemporary philosophers accept both play important roles.")
    
    user_question = st.text_area("Ask your own question:", placeholder="e.g., How do we know anything for certain?")
    
    if st.button("Ask AI Tutor") and user_question:
        st.write("**AI Response**: Your question touches on important epistemological issues. Consider reviewing the relevant modules and resources for detailed answers, or discuss with your instructor for personalized guidance.")

# Footer
st.markdown("---")
st.markdown("**PHL201 Epistemology | Developed by Xavier Honablue M.Ed | CognitiveCloud.ai**")
st.caption("Interactive Learning Platform for Theory of Knowledge")
