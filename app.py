import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# SECURE API KEY HANDLING
ANTHROPIC_API_KEY = st.secrets["ANTHROPIC_API_KEY"]

st.set_page_config(page_title="PHL201 Epistemology - CognitiveCloud.ai", layout="wide", initial_sidebar_state="expanded")

# Epistemology-focused questions - 35 total for maximum points
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
     "Knowledge has rational justification and corresponds to reality"),
    
    ("A posteriori knowledge requires:", 
     ["Pure reasoning only", "Experience and observation", "Mathematical proof", "Authority confirmation"], 
     "Experience and observation"),
    
    ("Internalism in epistemology holds that:", 
     ["Knowledge comes from within", "The factors that justify belief must be accessible to the believer", "Only internal states exist", "External world is irrelevant"], 
     "The factors that justify belief must be accessible to the believer"),
    
    ("Externalism in epistemology argues:", 
     ["Only external things exist", "Justification can depend on factors outside the believer's awareness", "Knowledge is impossible", "Only empirical knowledge counts"], 
     "Justification can depend on factors outside the believer's awareness"),
    
    ("The correspondence theory of truth states:", 
     ["Truth is what most believe", "Truth consists in agreement of thoughts with reality", "Truth is whatever works", "Truth doesn't exist"], 
     "Truth consists in agreement of thoughts with reality"),
    
    ("Epistemic circularity occurs when:", 
     ["Using circular reasoning", "Using a source of knowledge to validate itself", "Avoiding all reasoning", "Only trusting authorities"], 
     "Using a source of knowledge to validate itself"),
    
    ("The tripartite definition of knowledge requires:", 
     ["Only truth", "Belief, truth, and justification", "Only justification", "Only belief"], 
     "Belief, truth, and justification"),
    
    ("Fallibilism holds that:", 
     ["We can never be wrong", "Knowledge doesn't require absolute certainty", "All beliefs are false", "Only certain beliefs count as knowledge"], 
     "Knowledge doesn't require absolute certainty"),
    
    ("The regress problem in epistemology concerns:", 
     ["Going backwards in time", "The infinite chain of justification for beliefs", "Forgetting information", "Repeating mistakes"], 
     "The infinite chain of justification for beliefs"),
    
    ("Virtue epistemology focuses on:", 
     ["Moral virtues only", "Intellectual virtues and excellences in knowing", "Social virtues", "Physical abilities"], 
     "Intellectual virtues and excellences in knowing"),
    
    ("Contextualism in epistemology claims:", 
     ["Context never matters", "Knowledge attributions are context-sensitive", "Only context matters", "Context is irrelevant to truth"], 
     "Knowledge attributions are context-sensitive"),
    
    ("The value problem asks:", 
     ["How much knowledge costs", "Why knowledge is more valuable than mere true belief", "Which knowledge is most important", "How to measure knowledge"], 
     "Why knowledge is more valuable than mere true belief"),
    
    ("Modal epistemology deals with:", 
     ["Only necessary truths", "Knowledge of possibility and necessity", "Only empirical facts", "Only logical truths"], 
     "Knowledge of possibility and necessity"),
    
    ("What distinguishes knowledge from lucky guesses?", 
     ["Knowledge is always certain", "Knowledge has proper justification and isn't accidental", "Knowledge is more popular", "Knowledge is simpler"], 
     "Knowledge has proper justification and isn't accidental"),
    
    ("According to course readings, precise definition matters because:", 
     ["It sounds academic", "Imprecise claims cannot be properly evaluated", "It makes arguments longer", "It confuses opponents"], 
     "Imprecise claims cannot be properly evaluated"),
    
    ("The law of non-contradiction states:", 
     ["Everything contradicts", "Something cannot both be and not be in the same respect at the same time", "All contradictions are true", "Logic is impossible"], 
     "Something cannot both be and not be in the same respect at the same time")
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
        "Epistemology Quiz", 
        "Visualizations", 
        "Key Definitions",
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
            
            # Interactive LLM Discussion
            st.markdown("---")
            st.subheader("Discuss Your Responses with AI")
            
            # Initialize discussion history for this module
            if 'module1_discussion' not in st.session_state:
                st.session_state.module1_discussion = []
            
            # Question selector
            selected_q = st.selectbox("Choose a question to discuss:", [
                "Question 1: Something I'm confident I know",
                "Question 2: How I decide whether to believe new information", 
                "Question 3: Difference between knowing and being certain"
            ])
            
            # User response input
            user_response = st.text_area(
                "Share your thoughts on this question:",
                height=100,
                placeholder="Type your response to the selected question..."
            )
            
            if st.button("Discuss with AI Tutor", type="primary"):
                if user_response.strip():
                    try:
                        import anthropic
                        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
                        
                        # Create context-aware prompt based on selected question
                        if "Question 1" in selected_q:
                            context = """The student is responding to: "What's something you're confident you know?" 
                            This question explores the nature of confidence in knowledge claims and helps students examine their own epistemic commitments."""
                        elif "Question 2" in selected_q:
                            context = """The student is responding to: "How do you decide whether to believe new information?" 
                            This question examines epistemic practices and criteria for belief formation."""
                        else:
                            context = """The student is responding to: "Is there a difference between knowing and being certain?" 
                            This question explores the relationship between knowledge and certainty, a key epistemological issue."""
                        
                        system_prompt = f"""You are an epistemology tutor engaging in Socratic dialogue with a PHL201 student. {context}

Your role is to:
1. Acknowledge their response thoughtfully
2. Ask 2-3 probing follow-up questions that deepen their thinking
3. Connect their response to key epistemological concepts (JTB, justification, sources of knowledge, etc.)
4. Help them see philosophical implications of their everyday examples
5. Encourage further reflection without being preachy

Be supportive but intellectually challenging. Help them discover insights rather than lecturing them."""

                        message = client.messages.create(
                            model="claude-3-sonnet-20240229",
                            max_tokens=800,
                            temperature=0.7,
                            system=system_prompt,
                            messages=[{
                                "role": "user", 
                                "content": f"Question: {selected_q}\n\nStudent response: {user_response}"
                            }]
                        )
                        
                        ai_response = message.content[0].text
                        
                        # Add to discussion history
                        st.session_state.module1_discussion.append({
                            "question": selected_q,
                            "student_response": user_response,
                            "ai_response": ai_response
                        })
                        
                        # Display the discussion
                        st.markdown("### AI Tutor Response")
                        st.markdown(f"**Your Response**: {user_response}")
                        st.markdown(f"**AI Tutor**: {ai_response}")
                        
                    except Exception as e:
                        st.error("AI discussion temporarily unavailable. Please reflect on the questions independently.")
            
            # Display previous discussions
            if st.session_state.module1_discussion:
                st.markdown("### Previous Discussions")
                for i, discussion in enumerate(st.session_state.module1_discussion):
                    with st.expander(f"Discussion {i+1}: {discussion['question']}"):
                        st.markdown(f"**Your Response**: {discussion['student_response']}")
                        st.markdown(f"**AI Tutor**: {discussion['ai_response']}")
                
                if st.button("Clear Discussion History"):
                    st.session_state.module1_discussion = []
                    st.rerun()
    
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
        
        with st.expander("Interactive Discussion: Your Knowledge Claims"):
            st.write("**Reflection Prompts:**")
            st.write("- Think of a belief you hold strongly. What makes it knowledge vs. opinion?")
            st.write("- Describe a time you changed your mind about something. What convinced you?")
            st.write("- How do you handle disagreement with people you respect?")
            
            # LLM Discussion for Module 2
            if 'module2_discussion' not in st.session_state:
                st.session_state.module2_discussion = []
            
            discussion_prompt = st.text_area(
                "Share your thoughts on knowledge vs. belief:",
                height=100,
                placeholder="Describe a belief you hold and explain why you think it counts as knowledge..."
            )
            
            if st.button("Analyze with AI", key="mod2_discuss"):
                if discussion_prompt.strip():
                    try:
                        import anthropic
                        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
                        
                        system_prompt = """You are helping a student analyze their knowledge claims using epistemological concepts. 

Guide them to:
1. Identify whether their example meets the traditional criteria for knowledge (belief, truth, justification)
2. Examine the quality and source of their justification
3. Consider potential challenges or limitations
4. Distinguish knowledge from strongly held beliefs or opinions
5. Apply course concepts like JTB analysis

Ask probing questions that help them think more deeply about their epistemic commitments."""

                        message = client.messages.create(
                            model="claude-3-sonnet-20240229",
                            max_tokens=700,
                            temperature=0.7,
                            system=system_prompt,
                            messages=[{
                                "role": "user", 
                                "content": discussion_prompt
                            }]
                        )
                        
                        ai_response = message.content[0].text
                        
                        st.session_state.module2_discussion.append({
                            "student_input": discussion_prompt,
                            "ai_response": ai_response
                        })
                        
                        st.markdown("### Analysis")
                        st.markdown(f"**Your Example**: {discussion_prompt}")
                        st.markdown(f"**AI Analysis**: {ai_response}")
                        
                    except Exception as e:
                        st.error("Analysis temporarily unavailable.")
            
            # Show previous discussions
            if st.session_state.module2_discussion:
                st.markdown("### Previous Analyses")
                for i, disc in enumerate(st.session_state.module2_discussion):
                    with st.expander(f"Analysis {i+1}"):
                        st.markdown(f"**Your Example**: {disc['student_input']}")
                        st.markdown(f"**AI Analysis**: {disc['ai_response']}")
    
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
        
        with st.expander("Apply JTB Analysis"):
            st.write("**Test cases against the JTB conditions:**")
            st.write("Case 1: You believe your car is in the parking lot because you parked it there. It is there.")
            st.write("Case 2: You believe your lottery ticket will win because you 'feel lucky.' It wins.")
            
            # Interactive JTB Analysis
            if 'module3_discussion' not in st.session_state:
                st.session_state.module3_discussion = []
            
            user_case = st.text_area(
                "Describe your own example to test against JTB:",
                height=100,
                placeholder="Example: I believe/know that [something] because [reasons]..."
            )
            
            if st.button("Test with JTB Analysis", key="mod3_jtb"):
                if user_case.strip():
                    try:
                        import anthropic
                        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
                        
                        system_prompt = """You are helping a student apply the JTB (Justified True Belief) analysis to their example.

Systematically evaluate their case:
1. BELIEF: Do they believe the proposition?
2. TRUTH: Is the proposition actually true? (consider this carefully)
3. JUSTIFICATION: Do they have adequate reasons/evidence?

Then determine: Does this count as knowledge under the JTB analysis?
Consider potential problems: Is the justification strong enough? Could this be a Gettier-type case? 
Help them understand the analysis process."""

                        message = client.messages.create(
                            model="claude-3-sonnet-20240229",
                            max_tokens=600,
                            temperature=0.7,
                            system=system_prompt,
                            messages=[{
                                "role": "user", 
                                "content": f"Please analyze this case using JTB: {user_case}"
                            }]
                        )
                        
                        ai_response = message.content[0].text
                        
                        st.session_state.module3_discussion.append({
                            "case": user_case,
                            "analysis": ai_response
                        })
                        
                        st.markdown("### JTB Analysis Results")
                        st.markdown(f"**Your Case**: {user_case}")
                        st.markdown(f"**Analysis**: {ai_response}")
                        
                    except Exception as e:
                        st.error("JTB analysis temporarily unavailable.")
    
    elif module == "Module 4: The Gettier Problem":
        st.subheader("The Gettier Problem")
        st.write("In 1963, Edmund Gettier challenged the JTB definition with counterexamples.")
        
        st.write("**Gettier Case Example:**")
        st.write("Smith believes Jones will get the job and has 10 coins.")
        st.write("Smith concludes: 'The person who gets the job has 10 coins.'")
        st.write("Plot twist: Smith gets the job and also has 10 coins!")
        
        st.write("Smith has justified true belief but not knowledge - it's just lucky coincidence.")
        
        with st.expander("Create Your Own Gettier Case"):
            st.write("**Gettier Case Pattern:**")
            st.write("1. Person has good evidence for false belief X")
            st.write("2. From X, they infer conclusion Y")
            st.write("3. By coincidence, Y happens to be true")
            st.write("4. Result: Justified true belief without knowledge")
            
            if 'module4_discussion' not in st.session_state:
                st.session_state.module4_discussion = []
            
            gettier_attempt = st.text_area(
                "Try creating your own Gettier-style case:",
                height=120,
                placeholder="Describe a scenario where someone has justified true belief but not knowledge..."
            )
            
            if st.button("Evaluate Gettier Case", key="mod4_gettier"):
                if gettier_attempt.strip():
                    try:
                        import anthropic
                        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
                        
                        system_prompt = """You are evaluating whether a student has successfully created a Gettier-style case.

A proper Gettier case needs:
1. Justified true belief (meets JTB conditions)
2. But intuitively NOT knowledge
3. The truth is accidental/lucky relative to the justification
4. The justification involves a false assumption

Analyze their attempt:
- Does it meet these criteria?
- Is the belief justified, true, but not knowledge?
- What makes it "gettiered"?
- How could they improve it if needed?

Be encouraging but precise about whether it works as a Gettier case."""

                        message = client.messages.create(
                            model="claude-3-sonnet-20240229",
                            max_tokens=600,
                            temperature=0.7,
                            system=system_prompt,
                            messages=[{
                                "role": "user", 
                                "content": f"Evaluate this potential Gettier case: {gettier_attempt}"
                            }]
                        )
                        
                        ai_response = message.content[0].text
                        
                        st.session_state.module4_discussion.append({
                            "attempt": gettier_attempt,
                            "evaluation": ai_response
                        })
                        
                        st.markdown("### Gettier Case Evaluation")
                        st.markdown(f"**Your Case**: {gettier_attempt}")
                        st.markdown(f"**Evaluation**: {ai_response}")
                        
                    except Exception as e:
                        st.error("Evaluation temporarily unavailable.")
    
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
        
        with st.expander("Classify Your Knowledge Sources"):
            st.write("**Think about how you learned different things:**")
            st.write("- Mathematical facts (2+2=4)")
            st.write("- Scientific facts (water boils at 100°C)")
            st.write("- Personal experiences (your birthday)")
            st.write("- Logical principles (if A=B and B=C, then A=C)")
            
            if 'module5_discussion' not in st.session_state:
                st.session_state.module5_discussion = []
            
            knowledge_example = st.text_area(
                "Describe something you know and how you learned it:",
                height=100,
                placeholder="I know that [something] and I learned this through [reason/experience/both]..."
            )
            
            if st.button("Analyze Knowledge Source", key="mod5_source"):
                if knowledge_example.strip():
                    try:
                        import anthropic
                        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
                        
                        system_prompt = """You are helping a student classify their knowledge according to rationalist vs. empiricist categories.

Analyze their example:
1. Is this a priori (knowable through reason alone) or a posteriori (requires experience)?
2. What role does reason play vs. sensory experience?
3. How does this fit with rationalist vs. empiricist approaches?
4. Are there elements of both reason and experience involved?

Help them see the complexity - most knowledge involves both rational and empirical elements. Connect to the historical debate between rationalists and empiricists."""

                        message = client.messages.create(
                            model="claude-3-sonnet-20240229",
                            max_tokens=600,
                            temperature=0.7,
                            system=system_prompt,
                            messages=[{
                                "role": "user", 
                                "content": f"Analyze the knowledge source in this example: {knowledge_example}"
                            }]
                        )
                        
                        ai_response = message.content[0].text
                        
                        st.session_state.module5_discussion.append({
                            "example": knowledge_example,
                            "analysis": ai_response
                        })
                        
                        st.markdown("### Knowledge Source Analysis")
                        st.markdown(f"**Your Example**: {knowledge_example}")
                        st.markdown(f"**Analysis**: {ai_response}")
                        
                    except Exception as e:
                        st.error("Analysis temporarily unavailable.")

elif page == "Epistemology Quiz":
    st.header("PHL201 Epistemology Knowledge Quiz")
    
    show_score()
    
    if st.session_state.current < len(st.session_state.questions):
        show_question()
    else:
        st.balloons()
        st.success(f"Quiz Complete! Final Score: {st.session_state.score} XP")
        
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

elif page == "Key Definitions":
    st.header("Essential Epistemology Definitions")
    st.markdown("**Comprehensive guide to key epistemological terms and concepts**")
    
    # Search functionality
    search_term = st.text_input("Search definitions:", placeholder="Type a term to search...")
    
    # Core epistemological definitions
    definitions = {
        "Epistemology": {
            "definition": "The branch of philosophy that studies the nature, sources, limits, and validity of knowledge",
            "example": "Epistemology asks questions like 'What is knowledge?' and 'How do we know what we know?'",
            "related": ["Knowledge", "Truth", "Justification"]
        },
        "Knowledge": {
            "definition": "Traditionally defined as justified true belief, though this definition faces challenges",
            "example": "You know it's raining if you believe it's raining, it actually is raining, and you have good reasons (like seeing/hearing rain)",
            "related": ["JTB", "Belief", "Truth", "Justification"]
        },
        "JTB (Justified True Belief)": {
            "definition": "The classical analysis of knowledge requiring three conditions: belief, truth, and justification",
            "example": "To know Paris is the capital of France, you must: (1) believe it, (2) it must be true, (3) have good reasons",
            "related": ["Knowledge", "Gettier Problem", "Belief", "Truth", "Justification"]
        },
        "A Priori Knowledge": {
            "definition": "Knowledge that can be known independently of experience through reason alone",
            "example": "Mathematical truths (2+2=4), logical principles (if A=B and B=C, then A=C)",
            "related": ["A Posteriori", "Rationalism", "Necessary Truth"]
        },
        "A Posteriori Knowledge": {
            "definition": "Knowledge that requires experience and observation to be known",
            "example": "Scientific facts (water boils at 100°C), historical events (World War II ended in 1945)",
            "related": ["A Priori", "Empiricism", "Contingent Truth"]
        },
        "Rationalism": {
            "definition": "The view that reason is the primary source of knowledge and that some knowledge is a priori",
            "example": "Descartes argued we can know 'I think, therefore I am' through reason alone",
            "related": ["A Priori", "Empiricism", "Innate Ideas", "Descartes"]
        },
        "Empiricism": {
            "definition": "The view that sensory experience is the primary source of knowledge",
            "example": "Locke argued the mind is a 'blank slate' filled through sensory experience",
            "related": ["A Posteriori", "Rationalism", "Sense Experience", "Locke"]
        },
        "Gettier Problem": {
            "definition": "Cases showing that justified true belief is not sufficient for knowledge due to luck or accident",
            "example": "Smith believes 'the person who gets the job has 10 coins' based on evidence about Jones, but Smith gets the job and happens to have 10 coins",
            "related": ["JTB", "Knowledge", "Lucky Truth", "Accidental Truth"]
        },
        "Skepticism": {
            "definition": "The philosophical position that questions whether knowledge is possible or achievable",
            "example": "Cartesian skepticism asks: How do you know you're not dreaming or being deceived by an evil demon?",
            "related": ["Doubt", "Certainty", "External World", "Descartes"]
        },
        "Foundationalism": {
            "definition": "The theory that knowledge has a foundation of basic beliefs that need no justification from other beliefs",
            "example": "Basic perceptual beliefs like 'I see red' might need no further justification",
            "related": ["Basic Beliefs", "Coherentism", "Justification", "Regress Problem"]
        },
        "Coherentism": {
            "definition": "The theory that beliefs are justified by how well they fit together in a coherent system",
            "example": "A belief is justified if it coheres with and is supported by other beliefs in your belief system",
            "related": ["Foundationalism", "Holism", "Web of Belief", "Justification"]
        },
        "Reliabilism": {
            "definition": "The theory that knowledge comes from reliable belief-forming processes",
            "example": "Vision is generally reliable, so beliefs formed through normal vision count as knowledge",
            "related": ["Process", "Reliability", "Externalism", "Goldman"]
        },
        "Internalism": {
            "definition": "The view that justifying factors must be accessible to the believer's consciousness",
            "example": "You can only be justified in believing something if you're aware of your reasons",
            "related": ["Externalism", "Access", "Justification", "Consciousness"]
        },
        "Externalism": {
            "definition": "The view that justifying factors can be external to the believer's awareness",
            "example": "Your belief might be justified by reliable processes even if you don't know they're reliable",
            "related": ["Internalism", "Reliabilism", "Environment", "Process"]
        },
        "Theoretical Thinking": {
            "definition": "Stenstad's term for thinking that seeks one correct view about reality, excluding different views",
            "example": "Scientific realism holds there's one true description of reality that science aims to discover",
            "related": ["Anarchic Thinking", "Objectivity", "Truth", "Stenstad"]
        },
        "Anarchic Thinking": {
            "definition": "Stenstad's term for thinking that accepts multiple valid perspectives without ruling them out",
            "example": "Different cultural approaches to understanding reality might all offer valid insights",
            "related": ["Theoretical Thinking", "Pluralism", "Perspectivism", "Stenstad"]
        },
        "Truth": {
            "definition": "The property of statements or beliefs that correspond to reality (correspondence theory)",
            "example": "The statement 'snow is white' is true if and only if snow is white",
            "related": ["Correspondence Theory", "Coherence Theory", "Pragmatic Theory"]
        },
        "Justification": {
            "definition": "The reason or evidence that supports a belief and makes it reasonable to hold",
            "example": "Your justification for believing it will rain might be dark clouds and weather forecasts",
            "related": ["Evidence", "Reasons", "Support", "Warrant"]
        },
        "Belief": {
            "definition": "A mental state of accepting or holding a proposition to be true",
            "example": "You believe Paris is in France - you accept this proposition as true",
            "related": ["Knowledge", "Opinion", "Acceptance", "Conviction"]
        },
        "Vague": {
            "definition": "Using words that are imprecise or whose boundaries are unclear",
            "example": "'Old people shouldn't drive' is vague because 'old' has unclear boundaries",
            "related": ["Ambiguous", "Precise", "Clear", "Definition"]
        },
        "Ambiguous": {
            "definition": "Using words that can have multiple possible meanings",
            "example": "'The bank is closed' could refer to a financial institution or riverbank",
            "related": ["Vague", "Multiple Meanings", "Context", "Interpretation"]
        },
        "Problem of the Criterion": {
            "definition": "The circular problem that we need criteria for truth to establish criteria for truth",
            "example": "To know what knowledge is, we need criteria, but to get criteria, we need to know what knowledge is",
            "related": ["Circularity", "Criteria", "Method", "Standards"]
        },
        "Fallibilism": {
            "definition": "The view that knowledge doesn't require absolute certainty - we can know things while acknowledging we might be wrong",
            "example": "We can know scientific facts even though future discoveries might revise them",
            "related": ["Certainty", "Doubt", "Revision", "Probability"]
        },
        "Virtue Epistemology": {
            "definition": "The theory that knowledge involves intellectual virtues like careful observation, critical thinking, and open-mindedness",
            "example": "A scientist who carefully checks their work displays intellectual virtues that contribute to knowledge",
            "related": ["Intellectual Virtues", "Character", "Excellence", "Sosa"]
        },
        "Contextualism": {
            "definition": "The view that knowledge attributions depend on context - the same belief might count as knowledge in one context but not another",
            "example": "In casual conversation you 'know' the bank is open, but when facing financial crisis you need higher standards",
            "related": ["Context", "Standards", "Practical Interests", "Skepticism"]
        }
    }
    
    # Filter definitions based on search
    if search_term:
        filtered_defs = {k: v for k, v in definitions.items() 
                        if search_term.lower() in k.lower() or 
                        search_term.lower() in v["definition"].lower()}
    else:
        filtered_defs = definitions
    
    # Display definitions
    if filtered_defs:
        for term, details in filtered_defs.items():
            with st.expander(f"**{term}**"):
                st.markdown(f"**Definition:** {details['definition']}")
                st.markdown(f"**Example:** {details['example']}")
                if details['related']:
                    related_terms = ", ".join(details['related'])
                    st.markdown(f"**Related Terms:** {related_terms}")
    else:
        st.warning("No definitions found matching your search term.")
    
    # Quick reference categories
    st.markdown("---")
    st.subheader("Browse by Category")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Core Concepts", use_container_width=True):
            st.session_state.def_filter = ["Epistemology", "Knowledge", "JTB", "Truth", "Belief", "Justification"]
        if st.button("Sources of Knowledge", use_container_width=True):
            st.session_state.def_filter = ["Rationalism", "Empiricism", "A Priori Knowledge", "A Posteriori Knowledge"]
    
    with col2:
        if st.button("Major Theories", use_container_width=True):
            st.session_state.def_filter = ["Foundationalism", "Coherentism", "Reliabilism", "Virtue Epistemology"]
        if st.button("Skepticism & Problems", use_container_width=True):
            st.session_state.def_filter = ["Skepticism", "Gettier Problem", "Problem of the Criterion"]
    
    with col3:
        if st.button("Course Concepts", use_container_width=True):
            st.session_state.def_filter = ["Theoretical Thinking", "Anarchic Thinking", "Vague", "Ambiguous"]
        if st.button("Show All", use_container_width=True):
            if 'def_filter' in st.session_state:
                del st.session_state.def_filter
    
    # Display filtered results if category selected
    if 'def_filter' in st.session_state:
        st.markdown("### Filtered Results")
        for term in st.session_state.def_filter:
            if term in definitions:
                details = definitions[term]
                with st.expander(f"**{term}**"):
                    st.markdown(f"**Definition:** {details['definition']}")
                    st.markdown(f"**Example:** {details['example']}")
                    if details['related']:
                        related_terms = ", ".join(details['related'])
                        st.markdown(f"**Related Terms:** {related_terms}")

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
