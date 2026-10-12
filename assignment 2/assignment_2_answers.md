# Assignment 2: AI and LLM Fundamentals

## 1. Self-Rating

My current self-assessment is:

| Topic | Rating | Explanation |
|---|---|---|
| Large Language Models (LLMs) | C | I understand the basic purpose of LLMs and how they generate text, but I need more practical experience building LLM-based applications independently. |
| Deep Learning | C | I understand the basic concepts of neural networks, but I need more hands-on experience implementing and tuning deep learning models. |
| Artificial Intelligence (AI) | B | I understand fundamental AI concepts and can implement basic AI-related solutions with documentation and some guidance. |
| Machine Learning (ML) | B | I understand basic ML workflows, including data preprocessing, model training, evaluation, and common algorithms. I can implement basic solutions with some guidance.


## 2. High-Level Architecture of an LLM Chatbot

### Overview

An LLM chatbot accepts a user's question, processes it, sends the relevant input to a Large Language Model, and returns a natural-language response.

### Architecture Components

1. **User Interface:** Accepts questions and displays responses through a web or chat interface.
2. **Backend API:** Receives user requests, validates inputs, and manages the conversation.
3. **Prompt Builder:** Combines the user's question, system instructions, and relevant conversation history.
4. **LLM:** Processes the prompt and generates a response.
5. **Response Handler:** Checks the generated response, handles errors, and returns the answer to the user.
6. **Monitoring and Security:** Applies authentication, input validation, rate limits, logging, and protection of sensitive information.

### Request Flow

User → Chat Interface → Backend API → Prompt Builder → LLM → Response Handler → User

### Optional RAG Extension

For a chatbot that answers questions from private documents, Retrieval-Augmented Generation (RAG) can be added:

1. Split documents into smaller chunks.
2. Convert the chunks into vector embeddings.
3. Store the embeddings and associated text in a vector database.
4. Convert the user's question into an embedding and retrieve relevant chunks.
5. Add the retrieved context to the prompt.
6. Send the augmented prompt to the LLM to generate a context-based answer.

### Benefits

- Provides natural-language interaction.
- Can use conversation context to produce relevant answers.
- RAG can ground responses in a specific document collection.
- Security controls and monitoring help make the application more reliable.

### Limitations

LLMs may generate incorrect or unsupported answers. RAG can reduce this risk but does not eliminate it. Sensitive data should be protected, and important answers should be validated.


## 3. Vector Databases and Technology Selection

### What Is a Vector Database?

A vector database stores and searches vector embeddings, which are numerical representations of text, images, or other data. These embeddings capture semantic features, allowing the system to find information based on meaning rather than exact keyword matches.

For example, a search for "how to secure a server" may retrieve a document titled "Server Hardening Best Practices," even if the wording is different.

### Hypothetical Problem

An organization needs an internal cybersecurity knowledge assistant. Employees should be able to ask questions about security policies, incident response procedures, and technical documentation. The chatbot should retrieve relevant internal documents and use an LLM to generate answers.

### My Choice: Qdrant

I would choose Qdrant as the vector database for this solution.

### Why Qdrant?

1. **Semantic search:** Finds relevant document chunks using vector similarity.
2. **Metadata filtering:** Filters results by document type, department, access level, or other metadata.
3. **Python integration:** Provides a Python client that can be integrated into a RAG application.
4. **Deployment flexibility:** Supports self-hosted deployment and managed cloud options.
5. **Scalability:** Supports indexing and searching vector collections as the document collection grows.

### High-Level Solution

1. Collect approved cybersecurity documents.
2. Split the documents into manageable text chunks.
3. Generate embeddings for each chunk using an embedding model.
4. Store the embeddings, text, and metadata in Qdrant.
5. When an employee asks a question, generate an embedding for the question.
6. Search Qdrant for the most relevant chunks, applying access-control filters.
7. Send the question and retrieved context to the LLM.
8. Return an answer with references to the relevant source documents.

### Important Security Considerations

Because the assistant handles internal cybersecurity information, it must enforce document-level permissions before returning search results. Sensitive information should be protected through authentication, authorization, encryption, and appropriate logging. The LLM should be instructed to answer from the retrieved evidence and acknowledge when the available information is insufficient.

### Conclusion

Qdrant is a suitable choice for this hypothetical project because it provides vector similarity search, metadata filtering, Python integration, and flexible deployment. These features make it a practical option for building a document-based RAG chatbot.