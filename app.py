**Case 3**: Sarah believes there are books in the library because libraries typically contain books. There are indeed books in the library.
            - Belief? ✓
            - Truth? ✓
            - Justification? ✓ (Reasonable inference from general knowledge)
            - **Conclusion**: Knowledge
            
            **Your Turn**: Think of something you believe you know. Does it satisfy all three JTB conditions?
            """)
    
    elif module == "Module 6: The Gettier Problem and Beyond":
        st.subheader("The Gettier Problem and Its Aftermath")
        
        st.markdown("""
        ## The Revolutionary Paper
        
        In 1963, Edmund Gettier published a three-page paper titled "Is Justified True Belief Knowledge?" that fundamentally changed epistemology. Gettier showed that the classical JTB analysis, accepted for over 2000 years, was insufficient. He presented cases where someone has justified true belief but intuitively lacks knowledge.
        
        ## Gettier's Original Cases
        
        **Case I: The Job Interview**
        
        Smith and Jones have applied for the same job. Smith has strong evidence for the following compound proposition:
        - Jones will get the job, AND Jones has 10 coins in his pocket
        
        Smith's evidence:
        - The company president told him Jones would get the job
        - Smith counted the coins in Jones's pocket
        
        From this, Smith infers: "The man who will get the job has 10 coins in his pocket"
        
        **The twist**: Unknown to Smith, he (Smith) will actually get the job, and Smith also happens to have 10 coins in his pocket.
        
        **Analysis**:
        - Smith believes "The man who will get the job has 10 coins"
        - This belief is TRUE (Smith gets the job and has 10 coins)
        - Smith has JUSTIFICATION (good evidence about Jones)
        - But intuitively, Smith doesn't KNOW this fact
        
        **Case II: The Sheep in the Field**
        
        Smith believes "Jones owns a Ford" based on strong evidence:
        - Jones has always owned a Ford
        - Jones just offered Smith a ride in a Ford
        - Jones says he owns a Ford
        
        Smith randomly selects these propositions:
        - Either Jones owns a Ford, or Brown is in Boston
        - Either Jones owns a Ford, or Brown is in Barcelona
        
        **The twist**: Jones doesn't actually own a Ford (he's been driving a rental), but Brown happens to be in Barcelona.
        
        **Analysis**:
        - Smith believes "Either Jones owns a Ford, or Brown is in Barcelona"
        - This belief is TRUE (Brown is in Barcelona)
        - Smith has JUSTIFICATION (evidence about Jones owning a Ford)
        - But Smith doesn't really KNOW this disjunction
        
        ## The Pattern in Gettier Cases
        
        **Common Structure**:
        1. The believer has strong evidence for a false proposition
        2. From this false proposition, they infer something else
        3. By coincidence, what they infer happens to be true
        4. Their justification is "gettiered" - disconnected from what makes their belief true
        
        **Key Insight**: The justification doesn't properly connect to the truth. There's an element of luck or accident that makes the belief true despite the flawed reasoning.
        
        ## More Gettier Cases
        
        **The Fake Barn Case** (Alvin Goldman):
        Henry is driving through the countryside and sees what appears to be a barn. He forms the belief "That's a barn." Unknown to Henry, he's in an area full of fake barn facades that look exactly like real barns from the road. However, the particular structure he's looking at happens to be the one real barn in the area.
        
        - Belief: "That's a barn" ✓
        - Truth: It is indeed a barn ✓
        - Justification: Normal visual experience ✓
        - Knowledge: Intuitively no - it's just luck he picked the real barn
        
        **The Stopped Clock Case**:
        You look at a clock that shows 3:00 PM and form the belief "It's 3:00 PM." The clock stopped exactly 24 hours ago, so it happens to show the correct time, but you have no way of knowing it's stopped.
        
        - Belief: "It's 3:00 PM" ✓
        - Truth: It is 3:00 PM ✓
        - Justification: Clock-reading is normally reliable ✓
        - Knowledge: No - it's accidental that the belief is true
        
        ## Responses to Gettier
        
        **1. The "No False Premises" Response**
        
        **Idea**: Add a fourth condition - the justification must not depend on any false beliefs.
        
        **Problem**: This seems too strong. Much of our knowledge seems to depend on beliefs that are technically false or at least imprecise.
        - "The Earth is round" (it's actually oblate)
        - "Water is H2O" (ignores isotopes and impurities)
        - Historical "knowledge" based on sources that contain some errors
        
        **2. Reliabilism**
        
        **Idea**: Focus on reliable belief-forming processes rather than justification accessible to the believer.
        
        **Alvin Goldman's version**: A belief is knowledge if it's true and produced by a reliable cognitive process.
        
        **Advantages**:
        - Handles Gettier cases (the processes in Gettier cases aren't fully reliable)
        - Explains animal and child knowledge
        - Connects to cognitive science
        
        **Problems**:
        - The generality problem: How specific should we be about the process?
        - Clairvoyance cases: What if someone has reliable but unjustified beliefs?
        - Cultural and social dimensions of knowledge
        
        **3. Causal Theories**
        
        **Idea**: Knowledge requires an appropriate causal connection between the fact and the belief.
        
        **Alvin Goldman's early version**: S knows that P if and only if the fact that P is causally connected in an appropriate way with S's believing P.
        
        **Advantages**:
        - Explains why Gettier cases fail (wrong causal chain)
        - Handles perceptual and memory knowledge well
        
        **Problems**:
        - What about mathematical and logical knowledge? (No clear causal connection)
        - General facts and laws (how are they causally connected to beliefs?)
        - Testimony (complex causal chains)
        
        **4. Defeasibility Theories**
        
        **Idea**: Knowledge is justified true belief that isn't defeated by any true proposition.
        
        **Lehrer and Paxson**: S knows P if S believes P, P is true, S is justified in believing P, and there is no true proposition that would defeat S's justification if S were justified in believing it.
        
        **Application to Gettier**: In Gettier cases, there are true propositions (like "Jones won't get the job") that would defeat the justification if known.
        
        **Problems**:
        - Misleading defeaters: What if true information would misleadingly defeat good justification?
        - The problem of specifying exactly what defeats what
        
        **5. Virtue Epistemology**
        
        **Idea**: Knowledge involves intellectual virtues or excellences.
        
        **Ernest Sosa**: Knowledge is true belief that manifests intellectual virtue.
        
        **Advantages**:
        - Connects epistemology to ethics
        - Emphasizes the quality of the believer's cognitive character
        - Can handle Gettier cases (they don't manifest virtue)
        
        **Problems**:
        - What exactly are intellectual virtues?
        - Can vicious people have knowledge?
        - Cultural relativity of virtues
        
        **6. Safety and Sensitivity Conditions**
        
        **Safety** (Ernest Sosa): S's belief that P is safe if S wouldn't easily have been wrong about P.
        
        **Sensitivity** (Robert Nozick): S's belief that P is sensitive if S wouldn't believe P if P were false.
        
        **Application**: Gettier cases typically involve beliefs that are unsafe (the person could easily have been wrong) or insensitive (they would have believed the same thing even if it were false).
        
        ## Contemporary Developments
        
        **Knowledge First Epistemology** (Timothy Williamson):
        - Knowledge is a primitive, unanalyzable mental state
        - Don't try to define knowledge in terms of belief, truth, and justification
        - Instead, use knowledge to understand these other concepts
        
        **Pragmatic Encroachment**:
        - Whether someone knows something depends partly on practical factors
        - Higher stakes require stronger evidence for knowledge
        - Challenges the traditional view that knowledge is purely epistemic
        
        **Experimental Philosophy**:
        - Use empirical methods to study intuitions about knowledge
        - Cross-cultural studies of epistemological concepts
        - Questions whether philosophers' intuitions are universal
        
        ## The Lasting Impact
        
        **What Gettier Showed**:
        - The classical JTB analysis is insufficient
        - Luck and accident can undermine knowledge even when all traditional conditions are met
        - The connection between justification and truth matters
        
        **What Gettier Didn't Show**:
        - That knowledge is impossible
        - That the three conditions aren't necessary
        - That we should abandon the project of analyzing knowledge
        
        **Current State**:
        - No consensus on the correct analysis of knowledge
        - Ongoing debate about whether knowledge can be analyzed at all
        - Rich variety of approaches and insights
        - Deeper understanding of the complexity of knowledge
        """)
        
        with st.expander("💡 Create Your Own Gettier Case"):
            st.markdown("""
            **Challenge**: Design a scenario where someone has justified true belief but not knowledge.
            
            **Template**:
            1. Set up a situation where someone has good evidence for belief X
            2. Make belief X false (unknown to the believer)
            3. Through coincidence, make the believer's conclusion true anyway
            4. The result: justified true belief without knowledge
            
            **Example**: 
            - You believe your friend is at the coffee shop because you saw their car outside
            - Actually, they lent their car to someone else and aren't there
            - But they happened to walk to the coffee shop and are there anyway
            - You have justified true belief that they're at the coffee shop, but not knowledge
            """)
    
    elif module == "Module 7: Skepticism and the Limits of Knowledge":
        st.subheader("Skepticism and the Limits of Knowledge")
        
        st.markdown("""
        ## What is Skepticism?
        
        **Skepticism** in philosophy is the view that questions whether knowledge is possible. Rather than denying that we have beliefs or that some beliefs are better than others, skepticism challenges whether any of our beliefs constitute genuine knowledge.
        
        **Types of Skepticism**:
        
        **Global Skepticism**: We cannot know anything at all
        **Local Skepticism**: We cannot know things in specific domains (external world, other minds, the future, morality, etc.)
        **Methodological Skepticism**: Using doubt as a tool to find certain knowledge (Descartes)
        **Pyrrhonian Skepticism**: Suspending judgment on all matters to achieve peace of mind
        
        ## Classical Skeptical Arguments
        
        **The Problem of the Criterion** (Sextus Empiricus):
        
        To know something, we need criteria for truth. But to establish criteria for truth, we need to know what truth is. This creates a circle:
        - To know, we need criteria
        - To have criteria, we need knowledge
        - Therefore, neither knowledge nor criteria are possible
        
        **The Regress Problem**:
        
        Any belief needs justification. But what justifies the justifying belief? This leads to:
        1. **Infinite regress**: Each belief needs another belief to justify it, ad infinitum
        2. **Circular reasoning**: Eventually beliefs justify each other in a circle
        3. **Foundationalism**: Some beliefs are basic and need no justification (but how do we know which ones?)
        
        ## Modern Skeptical Scenarios
        
        **Cartesian Doubt** (René Descartes):
        
        **The Evil Demon**: What if a powerful evil demon is deceiving you about everything? Your senses, your memories, even your mathematical beliefs could all be false. How could you tell the difference between reality and perfect deception?
        
        **Contemporary Versions**:
        - **Brain in a Vat**: What if you're just a brain in a vat being stimulated to have experiences of a world that doesn't exist?
        - **The Matrix**: What if you're plugged into a computer simulation like in the movie?
        - **Simulated Reality**: What if advanced beings are running a simulation of reality that includes you?
        
        **The Problem of the External World**:
        
        All you directly experience are your own mental states - sensations, perceptions, thoughts. How do you know these correspond to an external world? Maybe there are only minds and ideas, no material objects.
        
        **David Hume's Skepticism**:
        
        **Problem of Induction**: We cannot justify our belief that the future will resemble the past. Every inference from past experience to future expectations involves an unjustifiable leap.
        
        **Causation**: We never actually observe causal connections, only sequences of events. Our belief in causation is just psychological habit, not knowledge.
        
        **Personal Identity**: What makes you the same person over time? Your body changes, your mind changes, your memories are unreliable. There may be no enduring self.
        
        ## Arguments Against Skepticism
        
        **Moore's Common Sense Response**:
        
        G.E. Moore argued that we know common sense facts with greater certainty than any skeptical argument:
        - "Here is one hand, and here is another"
        - "I know this is a hand with greater certainty than I know any skeptical premise"
        - Therefore, skeptical arguments must have false premises
        
        **Problems with Moore's approach**:
        - Seems to miss the point of skeptical arguments
        - Doesn't explain how we know common sense facts
        - Vulnerable to the charge of begging the question
        
        **Transcendental Arguments**:
        
        **Strategy**: Show that skeptical scenarios are self-refuting or meaningless.
        
        **Example** (Kant): Experience requires categories like causation and substance. Therefore, we must be able to apply these categories to experience, which means we can have knowledge about the structure of experience.
        
        **Semantic Arguments** (Hilary Putnam):
        
        **Brain in a Vat argument**: If you were a brain in a vat, your words "brain" and "vat" would refer to simulated brains and vats, not real ones. So when you say "I am a brain in a vat," you're necessarily saying something false. Therefore, you're not a brain in a vat.
        
        **Problems**: Relies on controversial theories of meaning and reference.
        
        **Contextualist Responses**:
        
        **David Lewis, Keith DeRose**: Whether we "know" something depends on context. In ordinary contexts, we do have knowledge. Skeptical scenarios create artificially high standards that don't apply to normal life.
        
        **Relevant Alternatives Theory** (Fred Dretske):
        
        We only need to rule out relevant alternatives, not all logical possibilities. In normal contexts, brain-in-vat scenarios aren't relevant alternatives to consider.
        
        ## The Value and Function of Skepticism
        
        **Positive Roles of Skeptical Arguments**:
        
        **Philosophical Therapy**: Skepticism can cure us of dogmatism and overconfidence
        **Methodological Tool**: Doubt can help us find more secure foundations for knowledge
        **Clarification**: Skeptical challenges force us to be clearer about what we mean by "knowledge"
        **Humility**: Recognizing the limits of human knowledge can be wisdom
        
        **Practical Problems with Skepticism**:
        
        **Livability**: Can we actually live as skeptics? Don't we have to act on beliefs?
        **Self-refutation**: Does arguing for skepticism presuppose that we can know the skeptical arguments are sound?
        **Selectivity**: Skeptics seem to accept some forms of reasoning (logic, argument) while rejecting others
        
        ## Contemporary Developments
        
        **Epistemic Contextualism**:
        - Knowledge attributions are context-sensitive
        - "Knows" works like words such as "tall" or "rich"
        - Different contexts create different standards for knowledge
        
        **Epistemic Relativism**:
        - Knowledge claims are relative to communities, cultures, or frameworks
        - No absolute or universal standards for knowledge
        - What counts as knowledge varies across groups
        
        **Naturalized Epistemology**:
        - Focus on how we actually acquire beliefs rather than skeptical worries
        - Use psychology and cognitive science to understand knowledge
        - Abandon the traditional project of refuting skepticism
        
        **Pragmatist Approaches**:
        - Judge beliefs by their practical consequences rather than their correspondence to reality
        - Knowledge is what works for achieving our goals
        - Skeptical scenarios are irrelevant if they don't affect action
        
        ## Living with Uncertainty
        
        **Practical Rationality**: Even if we can't achieve certainty, we can still make reasonable decisions based on evidence and probability.
        
        **Degrees of Confidence**: Instead of claiming absolute knowledge, we can express varying degrees of confidence in our beliefs.
        
        **Fallibilism**: Accept that our beliefs might be wrong while still taking them seriously enough to act on.
        
        **Intellectual Humility**: Recognize the limits of human knowledge while continuing to seek truth and understanding.
        """)
        
        with st.expander("💡 Skeptical Challenge Exercise"):
            st.markdown("""
            **The Skeptical Challenge**:
            
            Pick something you're confident you know (e.g., "I'm currently reading text on a screen").
            
            **Step 1**: Consider skeptical alternatives
            - Could you be dreaming this?
            - Could you be in a simulation?
            - Could an evil demon be deceiving you?
            
            **Step 2**: Try to rule out these alternatives
            - What evidence could you give that you're not dreaming?
            - How could you prove you're not in a simulation?
            - Can you be certain there's no deception?
            
            **Step 3**: Reflect on the exercise
            - Does this undermine your original knowledge claim?
            - Are these skeptical scenarios relevant to practical life?
            - What does this tell us about the nature of knowledge and certainty?
            
            **Consider**: Maybe the goal isn't to achieve absolute certainty, but to have beliefs that are reasonable, well-supported, and useful for navigating life.
            """)
    
    elif module == "Module 8: Foundationalism vs. Coherentism":
        st.subheader("Foundationalism vs. Coherentism")
        
        st.markdown("""
        ## The Structure of Justification
        
        One of the central questions in epistemology is: **How is knowledge structured?** When we trace back our justifications for belief, what do we find? This leads to a fundamental debate about the architecture of human knowledge.
        
        ## The Regress Problem
        
        Consider any belief you hold - say, "It will rain tomorrow." If someone asks why you believe this, you might cite evidence: "The weather forecast says so." But why trust the weather forecast? "Because meteorologists use scientific methods." Why trust scientific methods? "Because they've been reliable in the past." But why think past reliability indicates future reliability?
        
        This questioning can continue indefinitely, leading to what philosophers call **the epistemic regress problem**:
        
        1. **Infinite Regress**: Each belief needs justification from another belief, ad infinitum
        2. **Circular Reasoning**: Eventually our beliefs justify each other in a circle  
        3. **Arbitrary Stopping Point**: We just declare some beliefs justified without reason
        4. **Foundationalism**: Some beliefs are basic and need no further justification
        5. **Coherentism**: Beliefs are justified by their place in a coherent system
        
        ## Foundationalism: The Quest for Bedrock
        
        **Core Idea**: Knowledge has a foundation-like structure. Some beliefs are **basic** (self-justifying or requiring no justification from other beliefs), while others are **non-basic** (justified by basic beliefs).
        
        ### Classical Foundationalism
        
        **Requirements for Basic Beliefs**:
        - **Infallible**: Cannot be false
        - **Indubitable**: Cannot be rationally doubted  
        - **Self-evident**: Their truth is obvious upon understanding them
        
        **Examples of Allegedly Basic Beliefs**:
        - **Immediate experience**: "I am having a red sensation now"
        - **Mathematical truths**: "2 + 2 = 4"
        - **Logical principles**: "Nothing can be both A and not-A"
        - **Simple conceptual truths**: "All bachelors are unmarried"
        
        **René Descartes' Foundation**:
        - Used methodological skepticism to find indubitable foundation
        - "Cogito ergo sum" (I think, therefore I am) as the basic belief
        - Clear and distinct ideas as the criterion for truth
        - Built knowledge from this certain foundation
        
        **Problems with Classical Foundationalism**:
        
        **The Given Myth** (Wilfrid Sellars): The idea that some experiences are "given" to us without conceptual interpretation is problematic. All conscious experience seems to involve concepts and interpretation.
        
        **Too Few Basic Beliefs**: If basic beliefs must be infallible, there are very few of them. Most of what we consider knowledge seems fallible.
        
        **The Inference Problem**: How do we get from basic beliefs about our mental states to knowledge about the external world? The gap seems unbridgeable.
        
        ### Modest Foundationalism
        
        **Relaxed Requirements**: Basic beliefs need not be infallible, just:
        - **Prima facie justified**: Justified unless there's defeating evidence
        - **Reliable**: Produced by generally trustworthy processes
        - **Properly basic**: Justified in certain circumstances without inference
        
        **Examples**:
        - **Perceptual beliefs**: "I see a red apple" (basic in normal conditions)
        - **Memory beliefs**: "I had breakfast this morning" (basic when memory is functioning)
        - **Introspective beliefs**: "I feel sad" (basic about one's own mental states)
        
        **Alvin Plantinga's Reformed Epistemology**:
        - Belief in God can be properly basic in certain circumstances
        - We have a sensus divinitatis that produces basic religious beliefs
        - These beliefs are warranted if produced by faculties aimed at truth
        
        ## Coherentism: The Web of Belief
        
        **Core Idea**: Beliefs are justified not by being basic, but by fitting coherently into a system of beliefs. Justification is holistic - it depends on how well beliefs work together.
        
        **W.V.O. Quine's Web of Belief**:
        - Our beliefs form a "web" where each belief is connected to others
        - Beliefs at the center (logic, mathematics) are more difficult to revise
        - Beliefs at the periphery (observational reports) are more easily changed
        - When experience conflicts with our beliefs, we can revise any part of the web
        
        **Keith Lehrer's Coherentism**:
        - A belief is justified if it coheres with the believer's acceptance system
        - The acceptance system includes beliefs, preferences, and principles
        - Coherence involves consistency, explanatory connections, and probabilities
        
        ### What Makes a System Coherent?
        
        **Consistency**: The beliefs in the system don't contradict each other
        
        **Comprehensiveness**: The system covers a wide range of the believer's experience
        
        **Explanatory Relations**: Beliefs explain and are explained by other beliefs in the system
        
        **Probabilistic Support**: Beliefs make other beliefs in the system more likely to be true
        
        **Simplicity**: Other things being equal, simpler systems are more coherent
        
        **Conservatism**: Systems that preserve more of our existing beliefs are preferred
        
        ### Advantages of Coherentism
        
        **Avoids Regress**: No need for basic beliefs that stop the regress arbitrarily
        
        **Holistic**: Matches how justification actually seems to work in science and everyday life
        
        **Democratic**: All beliefs can potentially serve as justifiers for others
        
        **Flexible**: Can accommodate new evidence by adjusting the entire system
        
        ### Problems with Coherentism
        
        **The Isolation Problem**: A coherent system might be completely cut off from reality. Coherent delusions are possible.
        
        **Alternative Systems Problem**: Multiple incompatible systems might be equally coherent. How do we choose between them?
        
        **Input Problem**: How does new experience get into the system if there are no basic experiential beliefs?
        
        **Circularity**: Coherentism seems to involve circular justification, which foundationalists reject.
        
        ## Hybrid Approaches
        
        ### Foundherentism (Susan Haack)
        
        **Combination**: Justification is partly foundational (some beliefs have independent warrant) and partly coherential (beliefs support each other).
        
        **Metaphor**: Knowledge is like a crossword puzzle - some clues (basic beliefs) provide independent reasons, but the answers must also fit together coherently.
        
        ### Contextualism
        
        **Context-Sensitivity**: What counts as basic or needs coherence depends on the epistemic context and the standards in play.
        
        **Different Domains**: Scientific knowledge might require coherence, while everyday perceptual knowledge might rely on foundations.
        
        ## Reliabilism and the Structure Debate
        
        **Process Reliabilism**: Focus on reliable belief-forming processes rather than the structure of justification.
        
        **Virtue Epistemology**: Emphasize intellectual virtues and proper cognitive functioning rather than foundational structure.
        
        **These approaches**: Suggest the foundation/coherence debate might be asking the wrong question by focusing too much on justification rather than reliable knowledge production.
        
        ## Implications for Practice
        
        **Scientific Method**:
        - **Foundationalist elements**: Observation reports as basic evidence
        - **Coherentist elements**: Theories must fit together with existing knowledge
        - **Hybrid reality**: Science uses both foundations and coherence
        
        **Legal Reasoning**:
        - **Basic evidence**: Eyewitness testimony, physical evidence
        - **Coherent case**: Evidence must tell a coherent story
        - **Standards vary**: Different standards for different types of cases
        
        **Everyday Knowledge**:
        - **Perceptual foundations**: We treat many sensory experiences as basic
        - **Coherence checking**: We reject beliefs that don't fit with what we know
        - **Pragmatic flexibility**: We adjust our standards based on practical needs
        """)
        
        with st.expander("💡 Structure Analysis Exercise"):
            st.markdown("""
            **Analyze Your Belief Structure**:
            
            Pick a complex belief you hold (e.g., "Climate change is primarily caused by human activity").
            
            **Foundationalist Analysis**:
            1. What basic evidence supports this belief?
            2. How does this evidence connect to your conclusion?
            3. Are there any beliefs you consider basic/foundational?
            
            **Coherentist Analysis**:
            1. How does this belief fit with your other beliefs?
            2. What other beliefs support this one?
            3. Would rejecting this belief require changing other beliefs?
            
            **Reflection**:
            - Which analysis better captures how you actually hold this belief?
            - Do you use both foundational evidence and coherence reasoning?
            - What happens when foundational evidence conflicts with system coherence?
            """)
    
    elif module == "Module 9: Theoretical vs. Anarchic Thinking":
        st.subheader("Theoretical vs. Anarchic Thinking")
        
        st.markdown("""
        ## Stenstad's Distinction
        
        In our course readings, philosopher Gail Stenstad makes an important distinction between two approaches to knowledge and truth. This distinction has significant implications for how we understand the nature of reality and our relationship to truth.
        
        ## Theoretical Thinking
        
        **Core Characteristics**:
        
        **Exclusivity**: If one view about reality is "correct," then any "different" view has to be "incorrect."
        
        **Unity of Truth**: There is one correct view about what the world is like.
        
        **Hierarchical Structure**: Views can be ranked as better or worse, more or less accurate.
        
        **Objective Standards**: There are universal criteria for determining truth that apply regardless of perspective or context.
        
        **Examples of Theoretical Approach**:
        - **Scientific Realism**: Science aims to discover the one true description of reality
        - **Mathematical Platonism**: Mathematical truths are objective and universal
        - **Moral Objectivism**: There are correct moral facts independent of what people believe
        - **Religious Fundamentalism**: One faith tradition has the complete truth about divine reality
        
        **Strengths of Theoretical Thinking**:
        - Provides clear standards for evaluation
        - Motivates rigorous inquiry and criticism
        - Allows for genuine disagreement and debate
        - Supports the idea of progress in knowledge
        - Maintains that some views are genuinely better than others
        
        **Problems with Theoretical Thinking**:
        - May be intolerant of alternative perspectives
        - Could miss valuable insights from different viewpoints
        - Might impose artificial unity on a diverse reality
        - Can lead to dogmatism and closed-mindedness
        - May not acknowledge the role of perspective in knowledge
        
        ## Anarchic Thinking
        
        **Core Characteristics**:
        
        **Pluralism**: Multiple "very different" perspectives can be valid simultaneously.
        
        **Non-exclusivity**: Different views are "not ruled out" even if they seem to conflict.
        
        **Contextual Truth**: Truth may be relative to perspective, culture, or framework.
        
        **Horizontal Structure**: Views are different rather than better or worse.
        
        **Examples of Anarchic Approach**:
        - **Cultural Relativism**: Different cultures have different valid ways of understanding reality
        - **Perspectivism**: Reality looks different from different viewpoints, and multiple perspectives are needed
        - **Postmodern Pluralism**: Grand narratives should be replaced by local, diverse understandings
        - **Religious Pluralism**: Different faith traditions offer complementary insights into divine reality
        
        **Strengths of Anarchic Thinking**:
        - Embraces diversity and different perspectives
        - Avoids dogmatism and intolerance
        - Recognizes the limitations of any single viewpoint
        - Can incorporate insights from multiple traditions
        - Acknowledges the role of context in shaping understanding
        
        **Problems with Anarchic Thinking**:
        - May lead to relativism where "anything goes"
        - Could undermine the possibility of genuine disagreement
        - Might prevent us from making necessary judgments
        - Can be paralyzed by too many equally valid options
        - May not adequately distinguish better from worse views
        
        ## Interpretive Challenges
        
        **The Ambiguity Problem**: As noted in our readings, Stenstad's claims about anarchic thinking are somewhat ambiguous. When she says different views are "not ruled out," what exactly does this mean?
        
        **Possible Interpretations**:
        
        **1. Logical Compatibility**: Views that don't logically contradict each other can both be true.
        - Example: "God is loving" and "God is just" can both be true
        - This seems reasonable but doesn't capture the radical nature of anarchic thinking
        
        **2. Contradictory Coexistence**: Even contradictory views can both be "true" in some sense.
        - Example: "God exists" and "God does not exist" are both acceptable
        - This seems to violate the law of non-contradiction
        
        **3. Framework Relativity**: Contradictory views are true relative to different frameworks.
        - Example: "God exists" is true within religious frameworks, false within naturalistic ones
        - This preserves logic but makes truth relative
        
        **4. Complementary Perspectives**: Different views capture different aspects of a complex reality.
        - Example: Wave and particle descriptions of light are both needed
        - This suggests reality is too complex for any single description
        
        ## Applications and Examples
        
        **In Science**:
        
        **Theoretical Approach**: Science aims to discover the one true theory that explains all phenomena. Competing theories are evaluated to determine which is correct.
        
        **Anarchic Approach**: Different scientific approaches (reductionist vs. holistic, quantitative vs. qualitative) offer complementary insights. No single method captures all of reality.
        
        **In Religion**:
        
        **Theoretical Approach**: One religion has the complete truth; other religions are false or incomplete.
        
        **Anarchic Approach**: Different religious traditions offer valid insights into spiritual reality. Multiple paths can lead to truth.
        
        **In Ethics**:
        
        **Theoretical Approach**: There are objective moral truths that apply universally. Moral disagreement reflects ignorance or error.    elif module == "Module 5: The Classical Definition of Knowledge (JTB)":
        st.subheader("The Classical Definition of Knowledge")
        
        st.markdown("""
        ## The Tripartite Analysis of Knowledge
        
        For over two millennia, philosophers largely agreed on what knowledge is. The **classical definition** states that knowledge is **Justified True Belief** (JTB). This seems intuitive - to know something, you must believe it, it must be true, and you must have good reasons for believing it.
        
        ## The Three Conditions
        
        **1. Belief Condition**
        
        You cannot know something you don't believe. This seems obvious:
        - If someone asks "Do you know what time it is?" and you respond "It's 3:00 PM, but I don't believe that's correct," we'd say you don't really know the time
        - Knowledge requires a mental commitment to the truth of the proposition
        - The belief can be implicit (shown through behavior) or explicit (consciously held)
        
        **Complications:**
        - **Degrees of belief**: Do you need complete confidence or just enough to act?
        - **Unconscious knowledge**: Can you know things you're not consciously aware of believing?
        - **Knowledge without belief**: Some argue you can know things you're reluctant to believe (like your own mortality)
        
        **2. Truth Condition**
        
        You cannot know falsehoods. This is non-negotiable:
        - "I know the Earth is flat" is impossible if the Earth is round
        - Knowledge is **factive**: If you know P, then P must be true
        - This distinguishes knowledge from mere belief, which can be false
        
        **Complications:**
        - **What is truth?**: Correspondence, coherence, or pragmatic theories?
        - **Changing truth**: If scientific theories change, did we ever have knowledge?
        - **Vague truths**: For vague statements, when exactly are they true or false?
        
        **3. Justification Condition**
        
        True belief isn't enough - you need good reasons. Consider these cases:
        
        **Lucky Guess**: You believe your lottery ticket will win because you have a "good feeling," and it actually wins. You had a true belief, but not knowledge, because your justification was inadequate.
        
        **Superstitious Belief**: You believe there will be an earthquake because you saw a black cat, and coincidentally there is one. True belief, but not knowledge.
        
        **What makes justification adequate?**
        - **Evidential support**: Good reasons that make the belief likely to be true
        - **Proper grounding**: The justification must be relevant to the truth of the belief
        - **Non-accidental connection**: The justification must reliably lead to truth
        
        ## Types of Justification
        
        **Foundationalist Justification**
        - Some beliefs are **basic** (don't need justification from other beliefs)
        - Non-basic beliefs are justified by basic ones
        - Example: "I see a red apple" might be basic; "There are apples in the store" is derived
        
        **Coherentist Justification**
        - Beliefs are justified by fitting coherently with other beliefs
        - No absolutely basic beliefs - justification is holistic
        - Like a web of beliefs that support each other
        
        **Reliabilist Justification**
        - Beliefs are justified if they're produced by reliable processes
        - Focus on the process rather than the person's reasons
        - Example: Vision is generally reliable, so visual beliefs are usually justified
        
        ## Historical Examples and Applications
        
        **Plato's Analysis**
        In the *Theaetetus*, Plato considers whether knowledge is:
        1. Perception (rejected - perception can be false)
        2. True belief (rejected - not sufficient)
        3. True belief with an account/explanation (closest to modern JTB)
        
        **Medieval Developments**
        - Islamic philosophers like Al-Ghazali refined the analysis
        - Aquinas integrated Aristotelian epistemology with Christian theology
        - Emphasis on the role of divine illumination in knowledge
        
        **Modern Epistemology**
        - Descartes: Knowledge requires certainty and clear/distinct ideas
        - Locke: Knowledge comes from sensation and reflection
        - Hume: Challenged the possibility of certain knowledge beyond impressions
        
        ## Problems with the JTB Account
        
        **The Generality Problem**
        - Which level of generality should we specify for justification?
        - "Belief formed by vision" vs. "belief formed by vision in good light" vs. "belief formed by vision in good light while wearing glasses"
        
        **The Problem of Stored Beliefs**
        - Do we need to be currently aware of our justification?
        - What about beliefs we formed long ago but can't remember how?
        
        **Cultural and Social Dimensions**
        - Does justification require individual reasons or can social/cultural factors count?
        - What about testimony and trusting others?
        
        ## Testing the JTB Analysis
        
        **Case Study 1: Testimonial Knowledge**
        - You believe Paris is the capital of France because your teacher told you
        - It's true that Paris is the capital of France
        - Is testimony from a reliable source adequate justification?
        - **Analysis**: Seems to meet JTB conditions, and we commonly accept this as knowledge
        
        **Case Study 2: Memory Knowledge**
        - You believe you had breakfast this morning because you remember doing so
        - You did have breakfast this morning
        - Is memory a reliable form of justification?
        - **Analysis**: Memory seems generally reliable, so this appears to be knowledge
        
        **Case Study 3: Perceptual Knowledge**
        - You believe there's a tree in front of you because you see it
        - There is indeed a tree in front of you
        - Is visual perception adequate justification?
        - **Analysis**: In normal conditions, vision seems highly reliable
        
        ## The Stability of the JTB Account
        
        For centuries, the JTB analysis seemed secure. It captured our intuitions about knowledge and provided a framework for epistemological inquiry. Philosophers debated:
        - What exactly constitutes adequate justification?
        - How much justification is enough?
        - Whether justification must be accessible to the believer
        
        But they generally agreed that these three conditions were necessary and sufficient for knowledge.
        
        This consensus was shattered in 1963 by a three-page paper that would revolutionize epistemology...
        """)
        
        with st.expander("💡 Apply the JTB Analysis"):
            st.markdown("""
            **Test these cases against the JTB conditions:**
            
            **Case 1**: Maria believes her car is in the parking lot because she parked it there this morning. Her car is indeed in the parking lot.
            - Belief? ✓ 
            - Truth? ✓ 
            - Justification? ✓ (Memory of parking it)
            - **Conclusion**: Knowledge
            
            **Case 2**: John believes his lottery ticket will win because he "feels lucky." By an incredible coincidence, his ticket actually wins.
            - Belief? ✓
            - Truth? ✓
            - Justification? ✗ (Feeling lucky isn't adequate justification)
            - **Conclusion**: Not knowledge (lucky guess)
            
            **Case 3**: Sarah believes there are books in the library because libraries typically contain books. Thereelif page == "🤖 Epistemology AI Tutor":
    st.header("🤖 Your Personal Epistemology Tutor")
    st.markdown("**Get expert help with knowledge, truth, and justification concepts**")
    
    try:
        import anthropic
        
        # Initialize Anthropic client
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        
        # Epistemology-specific suggested questions
        st.subheader("💡 Common Epistemology Questions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Knowledge & Truth:**")
            if st.button("What exactly is knowledge vs. true belief?", use_container_width=True):
                st.session_state.current_question = "I'm struggling to understand the difference between knowledge and true belief. Can you explain this with examples and discuss why justification matters?"
            
            if st.button("Help me understand the Gettier problem", use_container_width=True):
                st.session_state.current_question = "The Gettier problem seems to challenge justified true belief as the definition of knowledge. Can you walk me through this with clear examples?"
            
            if st.button("What's the problem of the criterion?", use_container_width=True):
                st.session_state.current_question = "I don't understand the problem of the criterion in epistemology. How is this circular and why does it matter?"
        
        with col2:
            st.markdown("**Sources & Methods:**")
            if st.button("Rationalism vs Empiricism - which is right?", use_container_width=True):
                st.session_state.current_question = "Can you help me understand the debate between rationalists and empiricists? Do we need both reason and experience for knowledge?"
            
            if st.button("A priori vs a posteriori knowledge", use_container_width=True):
                st.session_state.current_question = "What's the difference between a priori and a posteriori knowledge? Can you give clear examples of each?"
            
            if st.button("How do I avoid vague philosophical claims?", use_container_width=True):
                st.session_state.current_question = "Our readings mention avoiding vague and ambiguous claims. How do I make my philosophical arguments clearer and more precise?"
        
        # Initialize chat history
        if 'tutor_chat_history' not in st.session_state:
            st.session_state.tutor_chat_history = []
        
        # Handle suggested questions
        if 'current_question' in st.session_state:
            st.session_state.user_input = st.session_state.current_question
            del st.session_state.current_question
        
        # Chat interface
        st.subheader("💬 Ask Your Epistemology Expert")
        
        # Display chat history
        for i, (question, answer) in enumerate(st.session_state.tutor_chat_history):
            with st.container():
                st.markdown(f"**🧠 You:** {question}")
                st.markdown(f"**🤖 Tutor:** {answer}")
                st.markdown("---")
        
        # User input
        user_question = st.text_area(
            "Ask your epistemology question:",
            value=st.session_state.get('user_input', ''),
            height=100,
            placeholder="e.g., I'm confused about how coherentism differs from foundationalism..."
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            ask_button = st.button("🎓 Ask Expert", type="primary")
        with col2:
            if st.button("🗑️ Clear Chat"):
                st.session_state.tutor_chat_history = []
                st.rerun()
        
        if ask_button and user_question.strip():
            with st.spinner("🤔 Analyzing your epistemology question..."):
                try:
                    # Create specialized epistemology tutor prompt
                    system_prompt = """You are an expert epistemology tutor for PHL201, specializing in the theory of knowledge. Your role is to:

1. Explain epistemological concepts clearly and accurately
2. Help students understand knowledge, truth, justification, and belief
3. Use Socratic questioning to deepen understanding
4. Connect ideas to course readings and standard epistemological problems
5. Provide concrete examples to illustrate abstract concepts
6. Encourage rigorous philosophical thinking

Key course topics include:
- The nature and definition of knowledge (JTB and post-Gettier theories)
- Rationalism vs empiricism 
- A priori vs a posteriori knowledge
- The problem of the criterion
- Skepticism and its challenges
- Foundationalism vs coherentism vs reliabilism
- Theoretical vs anarchic thinking (as discussed in course readings)
- Avoiding vague and ambiguous claims in philosophical arguments
- Internalism vs externalism
- The Gettier problem and responses to it

Always:
- Give precise philosophical definitions
- Use clear examples to illustrate complex concepts
- Ask follow-up questions to test understanding
- Connect new concepts to what students already know
- Encourage critical thinking about knowledge claims
- Reference major epistemological debates and positions

Be encouraging but academically rigorous. Help students see why epistemology matters for understanding knowledge in all areas of life."""

                    # Get response from Claude
                    message = client.messages.create(
                        model="claude-3-sonnet-20240229",
                        max_tokens=800,
                        temperature=0.7,
                        messages=[{
                            "role": "user", 
                            "content": prompt
                        }]
                    )
                    
                    response = message.content[0].text
                    
                    # Add to reflection history
                    st.session_state.reflection_history[selected_topic].append((user_reflection, response))
                    
                    # Display the discussion
                    st.markdown("### Discussion")
                    st.markdown(f"**Your Reflection:** {user_reflection}")
                    st.markdown(f"**AI Response:** {response}")
                    
                except Exception as e:
                    st.error("AI discussion temporarily unavailable. Please reflect on the questions above.")
        
        # Display previous discussions
        if st.session_state.reflection_history[selected_topic]:
            st.markdown("### Previous Discussions")
            for reflection, response in st.session_state.reflection_history[selected_topic]:
                with st.expander(f"Discussion: {reflection[:50]}..."):
                    st.markdown(f"**Your Reflection:** {reflection}")
                    st.markdown(f"**AI Response:** {response}")
    
    elif selected_topic == "The Reliability of Our Senses":
        st.subheader("👁️ The Reliability of Our Senses")
        st.markdown("""
        **Reflection Prompt:** Our senses can deceive us - optical illusions, dreams that feel real, false memories.
        
        **Key Questions:**
        - Can you think of times your senses have misled you?
        - If our senses are unreliable, how can we trust empirical knowledge?
        - What does this mean for the empiricist claim that knowledge comes from experience?
        - How do we distinguish between reliable and unreliable sensory experiences?
        """)
    
    elif selected_topic == "Can We Trust Our Memory?":
        st.subheader("🧠 Can We Trust Our Memory?")
        st.markdown("""
        **Reflection Prompt:** Memory seems essential for knowledge, but research shows memory is reconstructive and often inaccurate.
        
        **Key Questions:**
        - How much of your knowledge depends on memory?
        - What happens to knowledge claims if memory is unreliable?
        - Can you distinguish between reliable and unreliable memories?
        - Does this pose a problem for personal identity and knowledge of the past?
        """)
    
    elif selected_topic == "The Role of Authority in Knowledge":
        st.subheader("👨‍🏫 The Role of Authority in Knowledge")
        st.markdown("""
        **Reflection Prompt:** Much of what we "know" comes from teachers, experts, books, and other authorities.
        
        **Key Questions:**
        - How do you decide which authorities to trust?
        - Is knowledge from authority really knowledge, or just belief?
        - What's the difference between appealing to legitimate vs. illegitimate authority?
        - How do we balance trust in experts with thinking for ourselves?
        """)
    
    elif selected_topic == "Skepticism and Certainty":
        st.subheader("❓ Skepticism and Certainty")
        st.markdown("""
        **Reflection Prompt:** Skeptics argue we can't be certain about knowledge claims. Maybe we're dreaming, or being deceived.
        
        **Key Questions:**
        - Is absolute certainty necessary for knowledge?
        - How do you respond to skeptical challenges like "How do you know you're not dreaming?"
        - What's the difference between reasonable doubt and skeptical doubt?
        - Can we live as skeptics, or is some trust in our faculties necessary?
        """)
    
    elif selected_topic == "The Value of Philosophical Doubt":
        st.subheader("🤔 The Value of Philosophical Doubt")
        st.markdown("""
        **Reflection Prompt:** Philosophy encourages us to question our assumptions and examine our beliefs critically.
        
        **Key Questions:**
        - What beliefs have you questioned through studying philosophy?
        - Is there value in doubting what seems obvious?
        - How do we balance healthy skepticism with practical decision-making?
        - What's the difference between philosophical doubt and everyday doubt?
        """)

# Footer
st.markdown("---")
st.markdown("**PHL201 Epistemology | Developed by Xavier Honablue M.Ed | CognitiveCloud.ai**")
st.caption("Interactive Learning Platform for Theory of Knowledge")229",
                        max_tokens=1500,
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
                    st.info("Please check your API connection and try again.")
    
    except ImportError:
        st.error("📦 Missing required library. Please install: `pip install anthropic`")
    
    # Study tips for epistemology
    st.markdown("---")
    st.subheader("💡 How to Excel in Epistemology")
    
    tip_cols = st.columns(3)
    with tip_cols[0]:
        st.markdown("""
        **🎯 Master Key Concepts**
        - Focus on the JTB definition and its problems
        - Understand the rationalism/empiricism debate
        - Practice identifying different types of knowledge claims
        """)
    
    with tip_cols[1]:
        st.markdown("""
        **🤔 Think Critically**
        - Question your own knowledge claims
        - Look for hidden assumptions in arguments
        - Practice the Socratic method on yourself
        """)
    
    with tip_cols[2]:
        st.markdown("""
        **📚 Apply Concepts**
        - Use course readings to clarify difficult points
        - Connect epistemology to other areas of knowledge
        - Practice constructing clear, non-vague arguments
        """)

elif page == "💭 Reflection Discussions":
    st.header("💭 Interactive Reflection Discussions")
    st.markdown("**Engage with key epistemological questions through AI-guided discussions**")
    
    # Select reflection topic
    reflection_topics = [
        "Knowledge vs. Opinion in Daily Life",
        "The Reliability of Our Senses", 
        "Can We Trust Our Memory?",
        "The Role of Authority in Knowledge",
        "Skepticism and Certainty",
        "The Value of Philosophical Doubt"
    ]
    
    selected_topic = st.selectbox("Choose a reflection topic:", reflection_topics)
    
    # Topic-specific reflection prompts
    if selected_topic == "Knowledge vs. Opinion in Daily Life":
        st.subheader("🤔 Knowledge vs. Opinion in Daily Life")
        st.markdown("""
        **Reflection Prompt:** Think about something you believed you "knew" but later discovered was just opinion or false belief. 
        
        **Key Questions:**
        - What made you think it was knowledge rather than opinion?
        - How did you discover your error?
        - What does this tell us about the difference between knowledge and belief?
        - How can we better distinguish knowledge from strongly held opinions?
        """)
        
        # AI Discussion Interface
        if 'reflection_history' not in st.session_state:
            st.session_state.reflection_history = {}
        
        if selected_topic not in st.session_state.reflection_history:
            st.session_state.reflection_history[selected_topic] = []
        
        user_reflection = st.text_area(
            "Share your thoughts and experiences:",
            height=150,
            placeholder="Describe a time when you thought you knew something but were wrong..."
        )
        
        if st.button("💬 Discuss with AI", type="primary"):
            if user_reflection.strip():
                # AI response for reflection discussion
                try:
                    import anthropic
                    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
                    
                    prompt = f"""You are facilitating a philosophical reflection discussion on knowledge vs. opinion. 
                    A student has shared: "{user_reflection}"
                    
                    Respond by:
                    1. Acknowledging their reflection thoughtfully
                    2. Asking 2-3 probing questions that deepen their thinking
                    3. Connecting their experience to epistemological concepts
                    4. Encouraging further reflection
                    
                    Be supportive but intellectually challenging. Help them see the philosophical significance of their experience."""
                    
                    message = client.messages.create(
                        model="claude-3-sonnet-20240import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import List, Dict, Optional
import random

# 🔐 SECURE API KEY HANDLING
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
    
    ("Epistemic closure refers to:", 
     ["Ending discussions", "If you know p and know that p implies q, then you know q", "Keeping knowledge secret", "Only experts can have knowledge"], 
     "If you know p and know that p implies q, then you know q"),
    
    ("What is the lottery paradox in epistemology?", 
     ["A puzzle about probability and knowledge claims", "A problem with random selection", "An issue with mathematical proofs", "A challenge to authority"], 
     "A puzzle about probability and knowledge claims"),
    
    ("According to course material, why is precise definition important in philosophy?", 
     ["To sound more academic", "Because imprecise claims cannot be properly evaluated", "To make arguments longer", "To confuse opponents"], 
     "Because imprecise claims cannot be properly evaluated")
]
