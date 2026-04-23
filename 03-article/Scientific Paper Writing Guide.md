# **Establishing Rigorous Scholarly Communication in Computational Linguistics: A Comprehensive Framework for the Comparative Analysis of Distributional and Transformer-Based Semantic Representations**

The production of a high-quality scientific paper in the intersection of computer science and mathematics requires a synthesis of technical precision, logical architecture, and a nuanced understanding of how information is processed by a target audience. For a first-year undergraduate, the transition into this domain involves moving beyond expository summaries toward the construction of a defensible argument built on formal axioms and empirical evidence.1 Scientific writing is not merely an end-product of research; it is a fundamental part of the research process that forces the researcher to codify vague concepts into concrete, communicable ideas.1 The following guide establishes the standards for writing a comparative paper on Latent Semantic Analysis (LSA) and the all-MiniLM-L6-v2 transformer model, emphasizing quality of prose, structural integrity, and disciplinary rigor.

## **High-level principles of scientific writing in computer science and mathematics**

A strong scientific paper in the computational and mathematical sciences is defined by its ability to tell a coherent story through a "rational reconstruction" of the research.2 This principle dictates that the paper should not reflect the actual, often messy, chronological history of the research—including its false starts, debugging phases, and near-misses—but rather an idealized history that perfectly motivates each step of the solution.2 The goal is to make the final findings appear as an inevitable conclusion of the established logic, essentially convincing the reader that the solution is trivial once the correct framework is applied.2  
The distinction between a strong and a weak paper often lies in the clarity of its contribution. In computer science, a contribution generally falls into the categories of insight (explaining an existing phenomenon), performance (improving upon an existing benchmark), or capability (enabling a new task).3 A weak paper remains elusive about its purpose, providing a "laundry list" of experiments without a cohesive theme or a clearly stated hypothesis.3 For the comparison of LSA and all-MiniLM-L6-v2, the paper must identify exactly which representational or algebraic property is being investigated, such as the impact of linear versus non-linear transformations on semantic similarity.5  
Precision and "mercy on the reader" are the dual pillars of mathematical writing.2 This means every symbol must be defined before use, and the notation must be consistent and unambiguous.7 A paper that assumes too much prior knowledge alienates the reader, while one that provides too much general discipline knowledge becomes tedious.8 The ideal state of a paper is to be self-contained, ensuring that a peer at the same level (e.g., another first-year undergraduate) can follow the reasoning without requiring external references for the core argument.8

## **Section-by-section writing guide**

### **Title**

The title serves as the first point of interaction and the primary tool for indexing. Its purpose is to encapsulate the paper’s scope and variables succinctly.10 A strong title avoids unnecessary complexity while remaining highly informative.

* **What to include:** The specific models (LSA and all-MiniLM-L6-v2), the nature of the comparison (algebraic and representational), and the domain (sentence embeddings).  
* **What to avoid:** Vague phrases like "A Study of," "Investigation into," or sensationalist language. Avoid acronyms unless they are universally known.  
* **Common mistakes:** Titles that are either too broad (e.g., "Language Models Compared") or too verbose (e.g., "A Very Detailed and Exhaustive Look at the Differences Between Latent Semantic Analysis and the all-MiniLM-L6-v2 Model Using Various Tests").  
* **Strong wording:** "Representational Divergence in Sentence Embeddings: An Algebraic Comparison of Matrix Factorization and Transformer-Based Attention."  
* **Weak wording:** "Comparison of LSA and MiniLM." This is weak because it fails to specify *what* is being compared (performance, algebra, or use case).

### **Abstract**

The abstract is a standalone summary of the entire paper, typically between 200 and 300 words.10 It is not an introduction; it is a trailer that reveals the plot and the ending.12

* **What to include:** Motivation, the gap in existing research, the specific method of comparison, key results (including metrics), and the primary conclusion.9  
* **What to avoid:** Citations, complex mathematical notation, and detailed implementation steps.  
* **Common mistakes:** Being too vague about the results (e.g., "results were found to be interesting") or failing to mention the implications.4  
* **Template:** "Semantic representation has evolved from linear algebraic methods to neural architectures. However, a direct comparison of **\[Variable\]** between \*\*\*\* and **\[MiniLM\]** remains unquantified. This paper evaluates **\[Method\]** on \*\*\*\*. Results demonstrate that \*\*\*\*, suggesting that **\[Conclusion\]**."  
* **Strong wording:** "The findings indicate that the non-linear attention mechanism of all-MiniLM-L6-v2 resolves polysemy more effectively than the linear decomposition of LSA."  
* **Weak wording:** "We thought LSA might be worse than transformers. We were right. In this abstract we will explain why." This is weak because it uses first-person "we" and informal, imprecise language.

### **Introduction**

The introduction must establish the "tension" of the paper—why the research was necessary and what problem it solves.4 It should follow a "funnel" structure, moving from the broad field of distributional semantics to the specific comparison of LSA and all-MiniLM-L6-v2.15

* **What to include:** Broad context of vector space models, the shift from count-based to prediction-based models, the explicit research question, and a clear statement of the contribution.9  
* **What to avoid:** Long reviews of unrelated work or excessive "grandmothering" of general CS concepts.18  
* **Common mistakes:** Writing an introduction that is too long (over 10% of the paper) or failing to state the thesis.19  
* **Strong wording:** "While LSA has historically defined the standard for linear semantic extraction, the emergence of distilled transformers like all-MiniLM-L6-v2 challenges the sufficiency of document-level co-occurrence statistics."  
* **Weak wording:** "Everyone knows that AI is important. There are many ways to represent words. Two of them are LSA and MiniLM. I like both." This is weak because it is unprofessional and fails to motivate the research.

### **Background and Related Work**

This section provides the historical and technical context, showing how the current paper "emerges as the hero" of the narrative.21

* **What to include:** The origin of LSA in the 1980s as a solution to synonymy and polysemy, and the evolution of sentence transformers as a means to capture contextual nuance.22 Discuss the "distributional hypothesis"—that words occurring in similar contexts have similar meanings.22  
* **What to avoid:** A chronological list of papers. Instead, organize by theme (e.g., "Dimensionality Reduction" vs. "Representation Learning").3  
* **Strong wording:** "The transition from static embeddings, which assign a fixed vector to each term, to dynamic contextual embeddings reflects a shift in priority toward compositionality.27"  
* **Weak wording:** "First, Deerwester wrote about LSA in 1990\. Then, Vaswani wrote about Transformers in 2017\. Then, Reimers wrote about SBERT." This is weak because it is a "laundry list" rather than a synthesis.

### **Theoretical or mathematical framework**

This is the rigorous core of the paper. It defines the algebraic structures and operations that form the basis of the comparison.1

* **What to include:** Formal definitions of vector spaces $V$ and $W$. Explain LSA as a rank-reduced Singular Value Decomposition (SVD) of a term-document matrix $\\mathbf{A} \= \\mathbf{U \\Sigma V}^T$.22 Define the transformer's self-attention as a mapping of queries $\\mathbf{Q}$, keys $\\mathbf{K}$, and values $\\mathbf{V}$.30  
* **What to avoid:** "Notation for the sake of notation." Every symbol used must appear in subsequent analysis.32  
* **Common mistakes:** Mixing up row and column vectors, or failing to specify the dimensionality of the embedding space (e.g., 384 for MiniLM).33  
* **Strong version:** Use LaTeX for all math. "Let $\\mathbf{A} \\in \\mathbb{R}^{m \\times n}$ be a term-document matrix. LSA identifies the $k$-rank approximation $\\mathbf{A}\_k$ that minimizes the Frobenius norm error."  
* **Weak version:** "LSA uses SVD to make the matrix smaller. Then we get topics." This is weak because it lacks mathematical specificity and rigor.

### **Method and comparison criteria**

This section details how the comparison was performed so that it is reproducible.19

* **What to include:** The "grounds for comparison".36 Specify the task (e.g., Semantic Textual Similarity), the datasets used, and the evaluation metrics (e.g., Spearman's correlation, F1 score).37 Explain the pooling strategy (e.g., mean pooling) used to convert the transformer's token vectors into a single sentence embedding.39  
* **What to avoid:** Implementation details like variable names or specific IDEs, unless they are central to the argument.41  
* **Strong wording:** "To ensure a fair comparison, both methods were evaluated using cosine similarity on a shared corpus of 5,000 sentence pairs from the STS-B dataset."  
* **Weak wording:** "We ran the models on some sentences we found online and checked if they were right." This is weak because "some sentences" and "checked if they were right" are unscientific.

### **Analysis and Results**

This section presents the data objectively without extensive interpretation.42

* **What to include:** Markdown tables summarizing performance. Include metrics like inference speed (sentences per second), memory footprint (MB), and accuracy scores.44  
* **What to avoid:** Repeating in prose everything already visible in a table.19  
* **Common mistakes:** Presenting "data without meaning" or omitting the reporting of variability (e.g., standard deviation).14

| Model | Accuracy (STS-B) | Speed (Sent/Sec) | Embedding Dim |
| :---- | :---- | :---- | :---- |
| LSA (k=300) | 0.58 46 | \> 50,000 6 | 300 |
| all-MiniLM-L6-v2 | 0.82 44 | 14,200 47 | 384 |

* **Strong wording:** "As illustrated in Table 1, all-MiniLM-L6-v2 achieved a 24% improvement in accuracy over LSA, albeit with a significant reduction in processing throughput."  
* **Weak wording:** "The transformer was 0.82 and LSA was 0.58. This shows the transformer is better." This is weak because it uses the word "better" without nuance and lacks descriptive context.

### **Discussion**

The discussion is where the results are interpreted, extrapolated, and connected back to the theoretical framework.4

* **What to include:** Explain *why* the results occurred. For instance, LSA's "syntactic blindness" prevents it from distinguishing "The treatment worked" from "The treatment didn't work".6 Contrast this with the transformer’s positional encodings.30  
* **What to avoid:** Introducing new data or repeating the results section verbatim.43  
* **Strong wording:** "The observed performance gap suggests that the transformer’s self-attention mechanism effectively captures the 'nominal-participant-set bias' required for semantic judgment, a feature absent in LSA’s bag-of-words approach.51"  
* **Weak wording:** "Maybe the transformer was better because it has more parameters. LSA is just a matrix thing." This is weak because "maybe" is poor hedging and "matrix thing" is colloquial.

### **Conclusion**

The conclusion summarizes the contribution and suggests future directions.2

* **What to include:** A final statement on the algebraic relationship between the two models and a suggestion for how researchers might choose between them based on resources.13  
* **What to avoid:** Simply repeating the abstract or listing limitations (which should be in the discussion).50  
* **Strong wording:** "In conclusion, while all-MiniLM-L6-v2 provides the representational depth necessary for nuanced semantic search, LSA remains a competitive baseline for high-throughput, document-level topic modeling where word order is secondary."  
* **Weak wording:** "This project showed that transformers are fast and LSA is slow sometimes. I learned a lot about NLP." This is weak because it focuses on the author's learning journey rather than scientific knowledge.

## **Topic-specific advice for this paper**

### **Writing well about vector spaces and embeddings**

For a first-year student, a vector space must be treated as a formal algebraic structure, not just a list of numbers. In computational linguistics, the vector space represents a manifold where semantic meaning is operationalized as geometric distance.55 When discussing all-MiniLM-L6-v2, it is essential to specify that the embeddings are typically normalized to unit length, meaning they reside on the surface of a unit hypersphere $S^{d-1}$.57 This normalization ensures that the dot product is equivalent to the cosine similarity, which is the standard metric for comparing text embeddings.57

### **Dimensionality and the "Curse"**

Dimensionality must be discussed with precision. LSA typically reduces a high-dimensional, sparse term-document matrix to 100-300 latent dimensions to filter noise.6 In contrast, all-MiniLM-L6-v2 outputs a fixed 384-dimensional dense vector.34 The author should explain the trade-offs: higher dimensionality allows for more conceptual precision but increases computational latency and risks the "curse of dimensionality," where distance measures become less meaningful.55

### **Linear versus non-linear structures**

A primary algebraic distinction between the two methods is the nature of their transformations. LSA is fundamentally linear, using SVD to find the best low-rank approximation of a matrix in the Frobenius norm.6 Sentence transformers, however, use non-linear activation functions and the softmax operation in self-attention.5 This non-linearity allows the model to learn complex, non-additive relationships between words that a linear model like LSA is mathematically incapable of representing.6

### **Interpretability and similarity structure**

There is a significant difference in how these models represent "meaning." LSA’s similarity structure is based on global co-occurrence, making it more interpretable: a dimension in LSA often corresponds to a latent "topic" or cluster of related words.63 Transformer embeddings are "distributed representations," where information is spread across all dimensions, making them "black boxes" that are difficult for humans to interpret directly.64

## **Research framing**

### **Formulating a comparative research question**

A research question (RQ) must go beyond descriptive "what" questions and address "how" or "why" relationships.66 It must be clear, focused, and measurable.67 Merely asking "Which is better?" is insufficient because "better" is subjective.

* **Effective RQ:** "How does the reduction of training data impact the representational stability of all-MiniLM-L6-v2 sentence embeddings compared to the linear topic extraction of LSA?".69  
* **Effective RQ:** "To what extent does the inclusion of positional encodings in all-MiniLM-L6-v2 allow for the representation of negation, a feature traditionally lost in LSA’s bag-of-words framework?".6

### **Stating contributions without exaggeration**

The researcher must distinguish between "what we did" and "what we found".41 Contributions should be stated modestly, using measured and specific claims.70 If the research demonstrates that LSA is nearly as effective as a transformer on a specific small dataset, the contribution is the identification of a cost-effective alternative for low-resource settings.13

### **Distinguishing claim types**

Rigorous scientific writing requires a clear separation between different types of statements. This is especially vital for a first-year student to master to avoid overstating empirical findings as mathematical laws.

| Statement Type | Definition | Example for this Topic |
| :---- | :---- | :---- |
| **Mathematical Claim** | Derived from axioms and logic. | "The SVD minimizes the Frobenius norm of the residual matrix." 22 |
| **Empirical Observation** | Derived from data/experiments. | "LSA’s throughput was five times higher than MiniLM’s." 47 |
| **Interpretation** | Explaining the significance. | "The higher accuracy suggests that context is vital for this task." 6 |
| **Speculation** | Hypothesizing future outcomes. | "Future models might integrate SVD into attention units." 5 |

### **Comparing two methods fairly**

A "fair" comparison requires all variables to be identical except for the methods in question.68 If comparing representational depth, the dimensionality should ideally be fixed for both models (e.g., by truncating LSA to 384 dimensions to match MiniLM).6 The author must also acknowledge the disparity in training data: all-MiniLM-L6-v2 was pre-trained on 1 billion pairs, while LSA is typically trained from scratch on the target corpus.44

## **Language and style**

### **Clear academic English**

Clarity is the objective, not complexity.1 The duty of the writer is to make reading the text as easy as possible.72 This is achieved by using the simplest word that accurately conveys the meaning.3 For example, use "use" instead of "utilize," which is often perceived as pretentious in CS writing.9

### **Conciseness and paragraphs**

Sentences should be short, direct, and focused on a single idea.2 The author should "cut the filler" and remove extraneous adjectives.2 Each paragraph must address a single message, ideally beginning with a "topic sentence" that encapsulates that message.2 A useful test is to read only the topic sentences of a draft; if the argument remains clear, the structural flow is sound.74

### **The correct use of hedging**

Hedging is the use of cautious language to distinguish "claims" from "facts".75 It is an essential element of humility in science, expressing a degree of uncertainty that protects the author from overgeneralization.77

* **Proper Hedging:** "The results *suggest* that LSA *may* struggle with complex syntactic structures.".78  
* **Excessive Hedging:** "It *might* be possible that one *could perhaps suggest* that..." This piles up qualifiers and weakens the argument.77  
* **Missing Hedging:** "LSA is better for large corpora." This is a definitive statement that is likely false in many contexts and requires qualification (e.g., "LSA *can be* more computationally efficient for...").4

### **Defining terms and notation**

The "mantra" of mathematical style is to define before use.8 Notation should be consistent throughout the document.80 A common convention in this field:

* Bold uppercase ($\\mathbf{A, U, Q}$) for matrices.22  
* Bold lowercase ($\\mathbf{v, u, h}$) for vectors.58  
* Standard italics ($x, y, \\theta$) for scalars and angles.81  
* Script letters ($\\mathcal{V, W}$) for vector spaces.81

## **Common mistakes and anti-patterns in CS and Math papers**

| Mistake | Why it is a problem | Bad Example | Improved Version |
| :---- | :---- | :---- | :---- |
| **Grandmothering** | Steals reader’s time with common knowledge.18 | "NLP is a field of computers that helps them read." | "Distributional semantics models the relationship between words and contexts." |
| **Ambiguous 'Present'** | Unclear if the work is yours or prior work.41 | "An algorithm is presented for topic extraction." | "This paper introduces a modified LSA algorithm for..." |
| **Connect the Quotes** | Fails to synthesize; shows no original evaluation.83 | Using three paragraphs of direct quotes from Vaswani (2017). | "Following Vaswani (2017), the current study utilizes self-attention because..." |
| **Starting with Symbols** | Syntactically awkward and confusing.32 | "$\\mathbf{Q}$ is the query matrix." | "The query matrix is denoted by $\\mathbf{Q}$." |
| **Ambiguous 'It'** | Obscures the subject of the sentence.11 | "MiniLM uses attention. It is fast." (What is fast?) | "The attention mechanism is fast due to parallelization." |
| **Rhetorical Overstatement** | Damages credibility and objectivity.29 | "Transformers have solved the problem of language." | "Transformers have significantly improved semantic retrieval accuracy." |
| **Inconsistent Tense** | Confuses the timeframe of the research.19 | Switching from past to future in the Method section. | Consistently use simple past for methods: "The corpus was tokenized." |

## **Practical blueprint for drafting the paper**

1. **Define the "Thread":** Identify the two or three points you want the reader to remember.2 Everything else should be omitted if it does not support these points.  
2. **Outline First:** Use a rough outline to divide the paper into small, handle-able pieces.12 Check the ordering of headers to ensure logical progression.26  
3. **Order of Writing:**  
   * **Phase 1:** Theoretical Framework and Method criteria (write while the implementation is fresh).85  
   * **Phase 2:** Results (report objectively using tables).43  
   * **Phase 3:** Discussion and Background (interpret results and contextualize).43  
   * **Phase 4:** Introduction and Conclusion (frame the final "story" once you know the ending).9  
   * **Phase 5:** Title and Abstract (write last to ensure they reflect the finished work).9  
4. **The "Topic Sentence" Review:** Read the first sentence of every paragraph. If they do not form a coherent narrative, the structure is broken and requires reorganization.21  
5. **Refine Notation:** Check every subscript and sign. Higham warns that sign errors are the most common and damaging mistakes in mathematical writing.33  
6. **External Review:** Have someone else read the document. Writers are often surprised by what is unclear to a fresh pair of eyes.14

## **Final checklist for self-review**

* **Contribution:** Is the "nugget"—the key insight—explicitly stated in the abstract and intro? 3  
* **Story:** Does the paper walk the reader through a logical journey with a clear beginning, middle, and end? 21  
* **Mathematical Precision:** Are all vectors, matrices, and scalars defined with consistent symbols? 7  
* **Reproduction:** Could another student implement this comparison based only on the details in the Method section? 29  
* **Objectivity:** Have subjective words like "best," "amazing," or "unbelievable" been removed? 70  
* **Visuals:** Do the tables and figures supplement the narrative rather than replace it? 11 Are they properly labeled? 72  
* **Citations:** Is every claim of fact backed by a recent, credible reference? 10 Are they in the correct format? 14  
* **Language:** Have all contractions been expanded (e.g., "don't" to "do not")? 50 Is the tone formal and academic? 88  
* **Brevity:** Has every redundant word or transition ("in other words," "the fact that") been removed? 2  
* **Completeness:** Are the results section and discussion section based on all variables promised in the introduction? 43

### ---

**Model outline for the paper**

1. **Introduction**  
   * The paradigm shift from linear algebra to neural attention in NLP.  
   * The problem: Lack of direct algebraic mapping between SVD and Attention.  
   * Research question: To what degree does non-linear attention resolve semantic ambiguity compared to linear matrix factorization?  
2. **Related Work**  
   * Foundations of LSA and the distributional hypothesis.  
   * The evolution of the Transformer and all-MiniLM-L6-v2.  
   * Previous comparative studies on static vs. dynamic embeddings.  
3. **Theoretical Framework**  
   * The SVD of document-term matrices: $\\mathbf{A} \= \\mathbf{U\\Sigma V}^T$.  
   * The mechanics of self-attention: Query, Key, and Value interactions.  
   * Contrast: Linear projection vs. weighted softmax attention.  
4. **Methodology**  
   * Datasets: STS-B and standardized clinical sentence pairs.  
   * Setup: Fixing the latent space to 384 dimensions for parity.  
   * Metrics: Cosine similarity and Spearman’s rank correlation.  
5. **Results**  
   * Performance accuracy on semantic similarity tasks.  
   * Throughput benchmarks: Sentences per second.  
   * Algebraic analysis: Sparsity of LSA vectors vs. density of Transformer embeddings.  
6. **Discussion**  
   * Why LSA fails on negation and word order.  
   * Interpretability: Topic association vs. distributed hidden states.  
   * The role of training scale (1 billion pairs vs. local corpus).  
7. **Conclusion**  
   * Summary of algebraic trade-offs.  
   * Final recommendation for model selection.  
   * Future work in hybrid semantic spaces.

### **Model abstract skeleton**

This study presents an algebraic and representational comparison of \*\*\*\* and the **\[all-MiniLM-L6-v2\]** sentence-transformer. While LSA utilizes \*\*\*\* to identify latent structures in a linear vector space, all-MiniLM-L6-v2 employs **\[Non-linear self-attention\]** to generate contextualized dense embeddings. The models were evaluated on the \*\*\*\* dataset using \*\*\*\* as the primary metric. Results indicate that \*\*\*\*, whereas \*\*\*\*. The analysis suggests that the divergence in representational quality is a result of \*\*\*\*. These findings contribute to the understanding of the trade-offs between **\[computational efficiency\]** and **\[semantic depth\]** in modern NLP architectures.

### **Model introduction skeleton**

The representation of natural language in a continuous vector space has revolutionized the field of computational linguistics **\[Citation\]**. Traditionally, \*\*\*\* provided a robust framework for uncovering hidden semantic factors through the **\[linear decomposition of term-document matrices\]** **\[Citation\]**. However, the emergence of transformer-based architectures like **\[all-MiniLM-L6-v2\]** has introduced a new paradigm of **\[context-sensitive neural embeddings\]** **\[Citation\]**. Despite the ubiquity of these neural models, a rigorous comparison of their underlying algebraic properties remains an essential area of study, particularly regarding **\[the impact of non-linear transformations on sentence-level meaning\]**. This study evaluates \*\*\*\* by **\[systematically measuring their representational stability and similarity structure\]**. The primary contribution of this work is the demonstration that \*\*\*\*.

### **10 high-impact rules for writing this paper well**

1. **Symbolic Sanity:** Explicitly state the shape and field of every matrix ($\\mathbf{M} \\in \\mathbb{R}^{m \\times n}$).  
2. **No "First-Person" Logic:** Instead of "We chose a threshold of 0.5," write "A threshold of 0.5 was selected because..."  
3. **Anchor on Geometry:** Use words like "manifold," "hypersphere," and "distance" to keep the math grounded in intuition.  
4. **Define the "Black Box":** Don't just say MiniLM is neural; explain the specific pooling layer that makes it a "sentence" model.  
5. **Be Boringly Consistent:** If you call it "all-MiniLM-L6-v2" in the title, do not call it "MiniLM" in the method and "the transformer" in the discussion.  
6. **Hedge with Modals:** Use "might," "could," and "suggests" for interpretations of the data.  
7. **Math is Poetry:** Higham suggests formulas should be easy to remember and pregnant with meaning; don't use nested subscripts unless unavoidable.  
8. **The "So What?" Test:** At the end of every paragraph in the Discussion, ask if you've explained why this finding matters for the reader.  
9. **Visual Parity:** If you have a table for MiniLM’s results, ensure the same categories are represented for LSA.  
10. **Mercy for the Reader:** Zobel’s rule: Clarity is much more vital for the author than the reader. Make the reader's job easy.

#### **Works cited**

1. Writing for Computer Science, accessed April 23, 2026, [https://elibrary-dev.nusamandiri.ac.id/assets/fileebook/210026.pdf](https://elibrary-dev.nusamandiri.ac.id/assets/fileebook/210026.pdf)  
2. Presenting your research: Writing NLP papers, accessed April 23, 2026, [http://web.stanford.edu/class/cs224u/2022/slides/cs224u-presenting-part2-handout.pdf](http://web.stanford.edu/class/cs224u/2022/slides/cs224u-presenting-part2-handout.pdf)  
3. Ten Tips for Writing CS Papers, Part 1 \- Sebastian Nowozin, accessed April 23, 2026, [https://www.nowozin.net/sebastian/blog/ten-tips-for-writing-cs-papers-part-1.html](https://www.nowozin.net/sebastian/blog/ten-tips-for-writing-cs-papers-part-1.html)  
4. The 5 Most Common Mistakes When Writing a Scientific Paper \- Dr Anna Clemens, accessed April 23, 2026, [https://annaclemens.com/blog/the-five-most-common-mistakes-when-writing-a-scientific-paper/](https://annaclemens.com/blog/the-five-most-common-mistakes-when-writing-a-scientific-paper/)  
5. Geometry Meets Attention: Interpretable Transformers via SVD Inspiration \- ResearchGate, accessed April 23, 2026, [https://www.researchgate.net/publication/393490190\_Geometry\_Meets\_Attention\_Interpretable\_Transformers\_via\_SVD\_Inspiration](https://www.researchgate.net/publication/393490190_Geometry_Meets_Attention_Interpretable_Transformers_via_SVD_Inspiration)  
6. What is Latent Semantic Analysis (LSA)? Complete Guide \- Articsledge, accessed April 23, 2026, [https://www.articsledge.com/post/latent-semantic-analysis-lsa](https://www.articsledge.com/post/latent-semantic-analysis-lsa)  
7. Handbook of Writing for the Mathematical Sciences, Second Edition, accessed April 23, 2026, [https://epubs.siam.org/doi/book/10.1137/1.9780898719550](https://epubs.siam.org/doi/book/10.1137/1.9780898719550)  
8. Gernot's Guide to Technical Writing, accessed April 23, 2026, [https://gernot-heiser.org/style-guide.html](https://gernot-heiser.org/style-guide.html)  
9. Tips for Writing NLP Papers. Over the years I've developed a certain… | by Vered Shwartz | Medium, accessed April 23, 2026, [https://medium.com/@vered1986/tips-for-writing-nlp-papers-9c729a2f9e1f](https://medium.com/@vered1986/tips-for-writing-nlp-papers-9c729a2f9e1f)  
10. A Guide to Writing a Scientific Paper: A Focus on High School Through Graduate Level Student Research \- PMC, accessed April 23, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3528086/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3528086/)  
11. Writing For Computer Science Chapter Summary | Justin Zobel \- Bookey, accessed April 23, 2026, [https://www.bookey.app/book/writing-for-computer-science](https://www.bookey.app/book/writing-for-computer-science)  
12. 9 Common Mistakes Students Make in Research (and How to Avoid Them), accessed April 23, 2026, [https://riseglobaleducation.com/blogs/most-common-mistakes-high-school-students-make-in-research](https://riseglobaleducation.com/blogs/most-common-mistakes-high-school-students-make-in-research)  
13. Comparative Evaluation of LSA-Based Summarization Against Traditional and Neural Approaches Using Cosine Similarity, accessed April 23, 2026, [https://saudijournals.com/media/articles/SB\_115\_98-104.pdf](https://saudijournals.com/media/articles/SB_115_98-104.pdf)  
14. 10 Common Mistakes to Avoid When Submitting a Research Paper (And How to Fix Them), accessed April 23, 2026, [https://ijirt.org/blog/posts/10-common-mistakes-to-avoid-when-submitting-a-research-paper-and-how-to-fix-them](https://ijirt.org/blog/posts/10-common-mistakes-to-avoid-when-submitting-a-research-paper-and-how-to-fix-them)  
15. 10 Common Mistakes to Avoid When Writing Scientific Papers \- Hello Bio, accessed April 23, 2026, [https://hellobio.com/blog/10-common-mistakes-to-avoid-when-writing-scientific-papers.html](https://hellobio.com/blog/10-common-mistakes-to-avoid-when-writing-scientific-papers.html)  
16. Writing a (Computer Science) Paper \- Jakob E. Bardram, MSc, PhD, accessed April 23, 2026, [https://www.bardram.net/wp-content/uploads/2017/12/Writing.Paper\_.pdf](https://www.bardram.net/wp-content/uploads/2017/12/Writing.Paper_.pdf)  
17. On the literary landscapes of vector embeddings | Computational Humanities Research, accessed April 23, 2026, [https://www.cambridge.org/core/journals/computational-humanities-research/article/on-the-literary-landscapes-of-vector-embeddings/5132C056AE4AE7816ACF1711447AD429](https://www.cambridge.org/core/journals/computational-humanities-research/article/on-the-literary-landscapes-of-vector-embeddings/5132C056AE4AE7816ACF1711447AD429)  
18. Three Sins of Authors in Computer Science and Math, accessed April 23, 2026, [https://www.cs.cmu.edu/\~jrs/sins.html](https://www.cs.cmu.edu/~jrs/sins.html)  
19. Writing scientific manuscripts: most common mistakes \- PMC \- NIH, accessed April 23, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5730143/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5730143/)  
20. 7 Common Mistakes Students Make in Research Writing (and How to Avoid Them) | by Sarahwesst | Medium, accessed April 23, 2026, [https://medium.com/@sarahwesst369/7-common-mistakes-students-make-in-research-writing-and-how-to-avoid-them-ec727097ae67](https://medium.com/@sarahwesst369/7-common-mistakes-students-make-in-research-writing-and-how-to-avoid-them-ec727097ae67)  
21. Technical Writing: Tips for Computer Scientists, accessed April 23, 2026, [https://personal.utdallas.edu/\~hamlen/hamlen-writingtips.pdf](https://personal.utdallas.edu/~hamlen/hamlen-writingtips.pdf)  
22. Latent semantic analysis \- Wikipedia, accessed April 23, 2026, [https://en.wikipedia.org/wiki/Latent\_semantic\_analysis](https://en.wikipedia.org/wiki/Latent_semantic_analysis)  
23. Latent semantic analysis, accessed April 23, 2026, [https://sites.socsci.uci.edu/\~lpearl/courses/readings/Evangelopoulos2013\_LatentSemAnalysis.pdf](https://sites.socsci.uci.edu/~lpearl/courses/readings/Evangelopoulos2013_LatentSemAnalysis.pdf)  
24. A Comparative Analysis of Sentence Transformer Models for Automated Journal Recommendation Using PubMed Metadata \- Preprints.org, accessed April 23, 2026, [https://www.preprints.org/manuscript/202501.1334/v1](https://www.preprints.org/manuscript/202501.1334/v1)  
25. From Word Vectors to Multimodal Embeddings: Techniques, Applications, and Future Directions For Large Language Models \- arXiv, accessed April 23, 2026, [https://arxiv.org/html/2411.05036v1](https://arxiv.org/html/2411.05036v1)  
26. The Challenge of Advanced Scientific Writing: Mistakes and Solutions \- Journals, accessed April 23, 2026, [https://journals.psu.edu/td/article/download/1619/1149/6921](https://journals.psu.edu/td/article/download/1619/1149/6921)  
27. Why and When to Use Sentence Embeddings Over Word Embeddings \- MachineLearningMastery.com, accessed April 23, 2026, [https://machinelearningmastery.com/why-and-when-to-use-sentence-embeddings-over-word-embeddings/](https://machinelearningmastery.com/why-and-when-to-use-sentence-embeddings-over-word-embeddings/)  
28. Compositionality and Sentence Meaning: Comparing Semantic Parsing and Transformers on a Challenging Sentence Similarity Dataset \- ACL Anthology, accessed April 23, 2026, [https://aclanthology.org/2025.cl-1.5.pdf](https://aclanthology.org/2025.cl-1.5.pdf)  
29. Crafting Papers on Machine Learning, accessed April 23, 2026, [https://icml.cc/Conferences/2002/craft.html](https://icml.cc/Conferences/2002/craft.html)  
30. Survey of transformers and towards ensemble learning using transformers for natural language processing \- PMC, accessed April 23, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10838835/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10838835/)  
31. Linear Algebra For Data Science In Depth | by Sunku Sankarsh \- Medium, accessed April 23, 2026, [https://medium.com/@sunkusankarsh/linear-algebra-for-data-science-in-depth-ae5a4d9efd94](https://medium.com/@sunkusankarsh/linear-algebra-for-data-science-in-depth-ae5a4d9efd94)  
32. Computer Science Writing, accessed April 23, 2026, [https://www.cs.toronto.edu/\~miller/Research/writing.html](https://www.cs.toronto.edu/~miller/Research/writing.html)  
33. The Most Common Errors in Undergraduate Mathematics, accessed April 23, 2026, [https://math.vanderbilt.edu/schectex/commerrs/](https://math.vanderbilt.edu/schectex/commerrs/)  
34. all-MiniLM-L6-v2 \- API Pricing & Providers \- OpenRouter, accessed April 23, 2026, [https://openrouter.ai/sentence-transformers/all-minilm-l6-v2](https://openrouter.ai/sentence-transformers/all-minilm-l6-v2)  
35. Highly Opinionated Advice on How to Write ML Papers — AI ..., accessed April 23, 2026, [https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers)  
36. How to Write a Comparative Analysis Throughout your academic career, you'll be asked to write papers in which you compare and co, accessed April 23, 2026, [https://cbs.umn.edu/sites/cbs.umn.edu/files/migrated-files/downloads/Compcontrastharvard.pdf](https://cbs.umn.edu/sites/cbs.umn.edu/files/migrated-files/downloads/Compcontrastharvard.pdf)  
37. Predicting Semantic Similarity Between Clinical Sentence Pairs Using Transformer Models: Evaluation and Representational Analysis \- PubMed, accessed April 23, 2026, [https://pubmed.ncbi.nlm.nih.gov/34037527/](https://pubmed.ncbi.nlm.nih.gov/34037527/)  
38. semantic similarity analysis using transformer-based sentence embeddings \- ResearchGate, accessed April 23, 2026, [https://www.researchgate.net/publication/394616542\_SEMANTIC\_SIMILARITY\_ANALYSIS\_USING\_TRANSFORMER-BASED\_SENTENCE\_EMBEDDINGS](https://www.researchgate.net/publication/394616542_SEMANTIC_SIMILARITY_ANALYSIS_USING_TRANSFORMER-BASED_SENTENCE_EMBEDDINGS)  
39. What's the difference between sentence-transformers and standard BERT for search?, accessed April 23, 2026, [https://milvus.io/ai-quick-reference/whats-the-difference-between-sentencetransformers-and-standard-bert-for-search](https://milvus.io/ai-quick-reference/whats-the-difference-between-sentencetransformers-and-standard-bert-for-search)  
40. Sentence-Transformers for Semantic Embeddings \- Emergent Mind, accessed April 23, 2026, [https://www.emergentmind.com/topics/sentence-transformers-for-semantic-embeddings](https://www.emergentmind.com/topics/sentence-transformers-for-semantic-embeddings)  
41. Some advice on writing well for NLP, accessed April 23, 2026, [https://psresnik.github.io/writing\_advice.html](https://psresnik.github.io/writing_advice.html)  
42. Five Common Mistakes in Scientific Writing and How to Avoid Them, accessed April 23, 2026, [https://scientificwriting.hcommons.org/2025/03/06/five-common-mistakes-in-scientific-writing-and-how-to-avoid-them/](https://scientificwriting.hcommons.org/2025/03/06/five-common-mistakes-in-scientific-writing-and-how-to-avoid-them/)  
43. Guide for scientific writing: how to avoid common mistakes in a scientific article \- Pepsic, accessed April 23, 2026, [https://pepsic.bvsalud.org/scielo.php?script=sci\_arttext\&pid=S0104-12822022000300341](https://pepsic.bvsalud.org/scielo.php?script=sci_arttext&pid=S0104-12822022000300341)  
44. What are some popular pre-trained Sentence Transformer models and how do they differ (for example, all-MiniLM-L6-v2 vs all-mpnet-base-v2)? \- Milvus, accessed April 23, 2026, [https://milvus.io/ai-quick-reference/what-are-some-popular-pretrained-sentence-transformer-models-and-how-do-they-differ-for-example-allminilml6v2-vs-allmpnetbasev2](https://milvus.io/ai-quick-reference/what-are-some-popular-pretrained-sentence-transformer-models-and-how-do-they-differ-for-example-allminilml6v2-vs-allmpnetbasev2)  
45. Justin Zobel Third Edition \- eBooks, accessed April 23, 2026, [https://content.e-bookshelf.de/media/reading/L-3921706-31955dbccc.pdf](https://content.e-bookshelf.de/media/reading/L-3921706-31955dbccc.pdf)  
46. Comparison of Latent Semantic Analysis and Vector Space Model for Automatic Identification of Competent Reviewers to Evaluate Papers, accessed April 23, 2026, [https://thesai.org/Downloads/Volume13No2/Paper\_9-Comparison\_of\_Latent\_Semantic\_Analysis.pdf](https://thesai.org/Downloads/Volume13No2/Paper_9-Comparison_of_Latent_Semantic_Analysis.pdf)  
47. Pretrained Models — Sentence Transformers documentation, accessed April 23, 2026, [https://www.sbert.net/docs/sentence\_transformer/pretrained\_models.html](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html)  
48. A Study of Sentence Similarity Based on the All-minilm- l6-v2 Model With "Same Semantics, Different Structure" After Fine Tuning \- Atlantis Press, accessed April 23, 2026, [https://www.atlantis-press.com/article/126004096.pdf](https://www.atlantis-press.com/article/126004096.pdf)  
49. From Rule-Based Systems to Transformers: A Journey through the Evolution of Natural Language Processing | by Omid (Saeid) Masoumzadeh, PhD | Medium, accessed April 23, 2026, [https://medium.com/@masoumzadeh/from-rule-based-systems-to-transformers-a-journey-through-the-evolution-of-natural-language-9131915e06e1](https://medium.com/@masoumzadeh/from-rule-based-systems-to-transformers-a-journey-through-the-evolution-of-natural-language-9131915e06e1)  
50. Common mistakes in scientific writing for CL, accessed April 23, 2026, [https://mjn.host.cs.st-andrews.ac.uk/teaching/cl-publishing.html](https://mjn.host.cs.st-andrews.ac.uk/teaching/cl-publishing.html)  
51. \[2301.13039\] Representation biases in sentence transformers \- arXiv, accessed April 23, 2026, [https://arxiv.org/abs/2301.13039](https://arxiv.org/abs/2301.13039)  
52. Representation biases in sentence transformers \- ACL Anthology, accessed April 23, 2026, [https://aclanthology.org/2023.eacl-main.268.pdf](https://aclanthology.org/2023.eacl-main.268.pdf)  
53. Common Mistakes in Research Papers & How to Avoid Them \- IOJH, accessed April 23, 2026, [https://iojh.com.bd/2025/03/28/common-mistakes-in-research-papers-how-to-avoid-them/](https://iojh.com.bd/2025/03/28/common-mistakes-in-research-papers-how-to-avoid-them/)  
54. How to choose the best model for semantic search \- Meilisearch, accessed April 23, 2026, [https://www.meilisearch.com/blog/choosing-the-best-model-for-semantic-search](https://www.meilisearch.com/blog/choosing-the-best-model-for-semantic-search)  
55. Choosing the Right Vector Embedding Model and Dimension: A School Analogy That Makes Everything Clear \- DEV Community, accessed April 23, 2026, [https://dev.to/sreeni5018/choosing-the-right-vector-embedding-model-and-dimension-a-school-analogy-that-makes-everything-1e1d](https://dev.to/sreeni5018/choosing-the-right-vector-embedding-model-and-dimension-a-school-analogy-that-makes-everything-1e1d)  
56. An intuitive introduction to text embeddings \- The Stack Overflow Blog, accessed April 23, 2026, [https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/](https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/)  
57. Embedding Similarity Explained: How to Measure Text Semantics | Thinking Sand \- Medium, accessed April 23, 2026, [https://medium.com/thinking-sand/embedding-similarity-explained-how-to-measure-text-semantics-2932a0d899c9](https://medium.com/thinking-sand/embedding-similarity-explained-how-to-measure-text-semantics-2932a0d899c9)  
58. Semantic Geometry of Sentence Embeddings \- ACL Anthology, accessed April 23, 2026, [https://aclanthology.org/2025.findings-emnlp.641.pdf](https://aclanthology.org/2025.findings-emnlp.641.pdf)  
59. Cosine Similarity: Formula, Examples & Use Cases | Tiger Data, accessed April 23, 2026, [https://www.tigerdata.com/learn/understanding-cosine-similarity](https://www.tigerdata.com/learn/understanding-cosine-similarity)  
60. From paragraph to graph: Latent semantic analysis for information visualization \- PMC \- NIH, accessed April 23, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC387298/](https://pmc.ncbi.nlm.nih.gov/articles/PMC387298/)  
61. Investigating Thematic Patterns and User Preferences in LLM Interactions using BERTopic, accessed April 23, 2026, [https://arxiv.org/html/2510.07557v1](https://arxiv.org/html/2510.07557v1)  
62. (PDF) A Survey of Text Representation and Embedding Techniques in NLP \- ResearchGate, accessed April 23, 2026, [https://www.researchgate.net/publication/369966528\_A\_Survey\_of\_Text\_Representation\_and\_Embedding\_Techniques\_in\_NLP](https://www.researchgate.net/publication/369966528_A_Survey_of_Text_Representation_and_Embedding_Techniques_in_NLP)  
63. Comparing Popular Embedding Models: Choosing the Right One for Your Use Case, accessed April 23, 2026, [https://dev.to/simplr\_sh/comparing-popular-embedding-models-choosing-the-right-one-for-your-use-case-43p1](https://dev.to/simplr_sh/comparing-popular-embedding-models-choosing-the-right-one-for-your-use-case-43p1)  
64. Dense and Sparse Embeddings: A Comprehensive Overview | by Mohamed Lokhandwala, accessed April 23, 2026, [https://mlokhandwalas.medium.com/dense-and-sparse-embeddings-a-comprehensive-overview-c5f6473ee9d0](https://mlokhandwalas.medium.com/dense-and-sparse-embeddings-a-comprehensive-overview-c5f6473ee9d0)  
65. Embedding space and static embeddings | Machine Learning \- Google for Developers, accessed April 23, 2026, [https://developers.google.com/machine-learning/crash-course/embeddings/embedding-space](https://developers.google.com/machine-learning/crash-course/embeddings/embedding-space)  
66. Developing research questions \- Library \- Monash University, accessed April 23, 2026, [https://www.monash.edu/library/help/assignments-research/developing-research-questions](https://www.monash.edu/library/help/assignments-research/developing-research-questions)  
67. Formulating Your Research Question (RQ) | Writing Studio | Vanderbilt University, accessed April 23, 2026, [https://www.vanderbilt.edu/writing/resources/handouts/research-question/](https://www.vanderbilt.edu/writing/resources/handouts/research-question/)  
68. Formulation of Research Question – Stepwise Approach \- PMC, accessed April 23, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6322175/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6322175/)  
69. Transformer versus traditional natural language processing: how ..., accessed April 23, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10461267/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10461267/)  
70. Academic Writing: Common Mistakes to Avoid and Best Practices to Follow \- Editor World, accessed April 23, 2026, [https://www.editorworld.com/article/dos-and-donts-of-academic-writing](https://www.editorworld.com/article/dos-and-donts-of-academic-writing)  
71. Supported encoder foundation models in watsonx.ai \- IBM, accessed April 23, 2026, [https://www.ibm.com/docs/en/watsonx/w-and-w/2.2.0?topic=models-supported-encoder](https://www.ibm.com/docs/en/watsonx/w-and-w/2.2.0?topic=models-supported-encoder)  
72. Scientific Writing: The Art of Programming Brains, accessed April 23, 2026, [https://www.mpinat.mpg.de/631838/guidelines\_english.pdf](https://www.mpinat.mpg.de/631838/guidelines_english.pdf)  
73. Writing a good scientific paper. The secrets I share with my students ..., accessed April 23, 2026, [https://medium.com/@black\_51980/writing-a-good-scientific-paper-c0f8af480c91](https://medium.com/@black_51980/writing-a-good-scientific-paper-c0f8af480c91)  
74. Best Practices in Academic Writing \- Valdosta State University, accessed April 23, 2026, [https://www.valdosta.edu/colleges/arts/art/documents/best-practices-in-academic-writing-.pdf](https://www.valdosta.edu/colleges/arts/art/documents/best-practices-in-academic-writing-.pdf)  
75. Hedging in Scientific Writing – Strategies & Techniques \- James Lind Institute, accessed April 23, 2026, [https://jliedu.ch/hedging-in-scientific-writing-strategies-techniques/](https://jliedu.ch/hedging-in-scientific-writing-strategies-techniques/)  
76. Hedging in Scientific and Social Texts \- Innovation Info, accessed April 23, 2026, [https://www.innovationinfo.org/articles/SJASR/SJASR-8-191.pdf](https://www.innovationinfo.org/articles/SJASR/SJASR-8-191.pdf)  
77. Effective Use of Hedging in Scientific Manuscripts: Advice to Non-Native English-Speaking Researchers \- PMC, accessed April 23, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10151619/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10151619/)  
78. Exploring Hedging Devices in Scientific Research Papers: A Content Analysis Study of the 'Medical Journal of the Islamic Republic of Iran' \- PMC, accessed April 23, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12584097/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12584097/)  
79. Writing Tips: Hedging in Scientific Writing \- BioMedical Editor, accessed April 23, 2026, [https://www.biomedicaleditor.com/hedging.html](https://www.biomedicaleditor.com/hedging.html)  
80. Writing for computer science zobel pdf, accessed April 23, 2026, [https://cdn.prod.website-files.com/6724adc7823aa3f4abd14525/6728c93bd5abb1abea68434b\_17544733926.pdf](https://cdn.prod.website-files.com/6724adc7823aa3f4abd14525/6728c93bd5abb1abea68434b_17544733926.pdf)  
81. 1 Vectors \- Cornell: Computer Science, accessed April 23, 2026, [https://www.cs.cornell.edu/courses/cs4220/2020sp/lec/2020-01-27.pdf](https://www.cs.cornell.edu/courses/cs4220/2020sp/lec/2020-01-27.pdf)  
82. What Is Cosine Similarity? | IBM, accessed April 23, 2026, [https://www.ibm.com/think/topics/cosine-similarity](https://www.ibm.com/think/topics/cosine-similarity)  
83. The Most Common Mistakes on Research Papers | UA Grantham, accessed April 23, 2026, [https://www.uagrantham.edu/blog/the-5-most-common-mistakes-on-research-papers/](https://www.uagrantham.edu/blog/the-5-most-common-mistakes-on-research-papers/)  
84. Avoid These Technical Writing Mistakes, accessed April 23, 2026, [https://www.csuci.edu/wmc/pdf/articles/rbly-technicalwriting.pdf](https://www.csuci.edu/wmc/pdf/articles/rbly-technicalwriting.pdf)  
85. Writing for Computer Science, accessed April 23, 2026, [https://faculty.kashanu.ac.ir/file/download/course/1677017074-justin-zobel-auth.-writing-for-computer-science-springer-verlag-london-2014-.pdf](https://faculty.kashanu.ac.ir/file/download/course/1677017074-justin-zobel-auth.-writing-for-computer-science-springer-verlag-london-2014-.pdf)  
86. Academic Writing for Computer Science \- cs.rit.edu, accessed April 23, 2026, [https://www.cs.rit.edu/\~rlaz/writing.html](https://www.cs.rit.edu/~rlaz/writing.html)  
87. Writing for Computer Science | Request PDF \- ResearchGate, accessed April 23, 2026, [https://www.researchgate.net/publication/313843504\_Writing\_for\_Computer\_Science](https://www.researchgate.net/publication/313843504_Writing_for_Computer_Science)  
88. What Is Academic Writing? | Dos and Don'ts for Students \- Scribbr, accessed April 23, 2026, [https://www.scribbr.com/category/academic-writing/](https://www.scribbr.com/category/academic-writing/)