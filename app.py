import streamlit as st
import hashlib
import re
import io
import os


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(37, 99, 235, 0.08),
            transparent 38%
        ),
        #080c14;
    color: #e8edf5;
}

.block-container {
    max-width: 1050px;
    padding-top: 34px;
    padding-bottom: 110px;
}


/* =====================================================
   SIDEBAR
   ===================================================== */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0d121c 0%,
            #0a0f17 100%
        );
    border-right: 1px solid #202b3b;
}

section[data-testid="stSidebar"] > div {
    padding-top: 28px;
}

.sidebar-brand {
    display: flex;
    align-items: center;
    font-size: 22px;
    font-weight: 750;
    color: #f8fafc;
    letter-spacing: -0.4px;
}

.sidebar-brand-icon {
    width: 32px;
    height: 32px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    margin-right: 9px;
    background:
        linear-gradient(
            135deg,
            #2563eb,
            #7c3aed
        );
    color: white;
    box-shadow:
        0 8px 22px rgba(37, 99, 235, 0.22);
}

.sidebar-description {
    color: #687589;
    font-size: 11px;
    margin-top: 5px;
    margin-left: 41px;
    letter-spacing: 0.2px;
}

.sidebar-heading {
    color: #566276;
    font-size: 9px;
    font-weight: 750;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    margin-top: 27px;
    margin-bottom: 9px;
}

.sidebar-card {
    background:
        linear-gradient(
            145deg,
            #121a26,
            #0f1621
        );
    border: 1px solid #202b3b;
    border-radius: 13px;
    padding: 14px 15px;
    color: #8995a7;
    font-size: 12px;
    line-height: 1.55;
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.02);
}

.sidebar-card strong {
    color: #dce4ef;
    font-weight: 650;
}

.sidebar-status {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    color: #9ba7b8;
    font-size: 11px;
}

.status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #22c55e;
    box-shadow:
        0 0 10px rgba(34,197,94,0.65);
}


/* =====================================================
   HERO
   ===================================================== */

.hero {
    text-align: center;
    margin-top: 8px;
    margin-bottom: 31px;
}

.hero-symbol {
    width: 58px;
    height: 58px;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 17px;
    background:
        linear-gradient(
            135deg,
            #2563eb 0%,
            #4f46e5 52%,
            #7c3aed 100%
        );
    color: white;
    font-size: 27px;
    box-shadow:
        0 14px 35px rgba(37, 99, 235, 0.23),
        0 5px 15px rgba(124, 58, 237, 0.12);
}

.hero-title {
    color: #f8fafc;
    font-size: 40px;
    font-weight: 780;
    letter-spacing: -1.8px;
    margin-top: 15px;
}

.hero-subtitle {
    color: #737f91;
    font-size: 14px;
    margin-top: 6px;
}


/* =====================================================
   UPLOAD
   ===================================================== */

.upload-title {
    color: #aeb8c8;
    font-size: 11px;
    font-weight: 650;
    letter-spacing: 0.3px;
    margin-bottom: 7px;
}

[data-testid="stFileUploader"] {
    background:
        linear-gradient(
            145deg,
            #101824,
            #0d141e
        );
    border: 1px solid #263347;
    border-radius: 17px;
    padding: 8px;
    transition: 0.2s ease;
    box-shadow:
        0 10px 35px rgba(0,0,0,0.13);
}

[data-testid="stFileUploader"]:hover {
    border-color: #376fe0;
    box-shadow:
        0 10px 38px rgba(37,99,235,0.10);
}


/* =====================================================
   DOCUMENT BAR
   ===================================================== */

.document-bar {
    display: flex;
    align-items: center;
    background:
        linear-gradient(
            135deg,
            #111a28,
            #0e1621
        );
    border: 1px solid #253246;
    border-radius: 15px;
    padding: 13px 16px;
    margin-top: 23px;
    margin-bottom: 29px;
    box-shadow:
        0 9px 30px rgba(0,0,0,0.12);
}

.document-icon {
    width: 42px;
    height: 42px;
    flex-shrink: 0;
    border-radius: 12px;
    background:
        linear-gradient(
            145deg,
            #172b61,
            #16234b
        );
    border: 1px solid #294178;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 13px;
    font-size: 19px;
}

.document-name {
    color: #edf2f8;
    font-size: 14px;
    font-weight: 680;
    max-width: 700px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.document-meta {
    color: #69768a;
    font-size: 10px;
    margin-top: 3px;
}


/* =====================================================
   WELCOME
   ===================================================== */

.welcome {
    text-align: center;
    padding: 34px 20px 23px;
}

.welcome-title {
    color: #e7edf5;
    font-size: 20px;
    font-weight: 680;
    letter-spacing: -0.2px;
}

.welcome-text {
    color: #687588;
    font-size: 12px;
    line-height: 1.65;
    margin-top: 8px;
}


/* =====================================================
   SUGGESTION CARDS
   ===================================================== */

.suggestion-box {
    background:
        linear-gradient(
            145deg,
            #111925,
            #0e151f
        );
    border: 1px solid #222e40;
    border-radius: 12px;
    padding: 12px 14px;
    color: #8995a7;
    font-size: 11px;
    margin-top: 7px;
    transition: all 0.2s ease;
}

.suggestion-box:hover {
    border-color: #34496a;
    color: #b6c0cf;
    transform: translateY(-1px);
}


/* =====================================================
   CHAT
   ===================================================== */

[data-testid="stChatMessage"] {
    border-radius: 17px;
    margin-top: 11px;
    margin-bottom: 11px;
    padding: 3px 4px;
    border: 1px solid transparent;
}

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-assistant"]
) {
    background:
        linear-gradient(
            145deg,
            #101722,
            #0d141e
        );
    border-color: #202c3d;
    box-shadow:
        0 8px 24px rgba(0,0,0,0.08);
}

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
) {
    background:
        linear-gradient(
            145deg,
            #131e31,
            #101a2a
        );
    border-color: #243653;
}

[data-testid="stChatMessageContent"] {
    color: #d8e0eb;
    font-size: 13.5px;
    line-height: 1.78;
}


/* =====================================================
   SOURCES
   ===================================================== */

.source-label {
    color: #58667a;
    font-size: 9px;
    font-weight: 750;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 11px;
    margin-bottom: 7px;
}

.source-pill {
    display: inline-block;
    background: #131c29;
    border: 1px solid #273449;
    color: #8b98ab;
    border-radius: 8px;
    padding: 4px 9px;
    font-size: 10px;
    margin-right: 5px;
    margin-bottom: 4px;
}


/* =====================================================
   CHAT INPUT
   ===================================================== */

[data-testid="stChatInput"] {
    border-color: #29374d !important;
}

[data-testid="stChatInput"] textarea {
    background: #101824 !important;
    color: #e7edf5 !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #59677a !important;
}


/* =====================================================
   STATUS
   ===================================================== */

[data-testid="stStatusWidget"] {
    background:
        linear-gradient(
            145deg,
            #101824,
            #0e151f
        );
    border: 1px solid #263348;
    border-radius: 13px;
}


/* =====================================================
   EXPANDER
   ===================================================== */

[data-testid="stExpander"] {
    background:
        linear-gradient(
            145deg,
            #101824,
            #0d141e
        );
    border: 1px solid #222e40;
    border-radius: 13px;
    margin-top: 20px;
}


/* =====================================================
   BUTTON
   ===================================================== */

.stButton > button {
    background:
        linear-gradient(
            135deg,
            #17243a,
            #131d2d
        );
    color: #aeb9c9;
    border: 1px solid #29384e;
    border-radius: 10px;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    color: #e5ebf4;
    border-color: #3b5d91;
    background:
        linear-gradient(
            135deg,
            #1a2a45,
            #17243a
        );
}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {
    text-align: center;
    color: #414d5e;
    font-size: 9px;
    margin-top: 60px;
    letter-spacing: 0.3px;
}


/* =====================================================
   HIDE STREAMLIT BRANDING
   ===================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "processed_pdf_hash": None,
    "pages_data": [],
    "chunks": [],
    "collection_name": None,
    "collection": None,
    "document_name": None,
    "embedding_dimension": 384,
    "chat_history": [],
    "document_ready": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# EMBEDDING MODEL
# =========================================================

@st.cache_resource(show_spinner=False)
def load_embedding_model():

    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


# =========================================================
# CHROMADB
# =========================================================

@st.cache_resource(show_spinner=False)
def get_chroma_client():

    import chromadb

    return chromadb.PersistentClient(
        path="./chroma_db"
    )


# =========================================================
# ANSWER CLEANING
# =========================================================

def clean_answer(answer):

    if not answer:
        return ""

    answer = re.sub(
        r"<[^>]*>",
        "",
        answer
    )

    answer = re.sub(
        r"\n{3,}",
        "\n\n",
        answer
    )

    return answer.strip()


# =========================================================
# NORMALIZE TEXT
# =========================================================

def normalize_text(text):

    text = str(text).lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# =========================================================
# STOP WORDS
# =========================================================

STOP_WORDS = {
    "what",
    "is",
    "are",
    "the",
    "a",
    "an",
    "of",
    "in",
    "on",
    "to",
    "for",
    "and",
    "or",
    "with",
    "who",
    "which",
    "where",
    "when",
    "how",
    "does",
    "do",
    "tell",
    "me",
    "about",
    "this",
    "that",
    "from",
    "was",
    "were",
    "be",
    "can",
    "could",
    "please",
    "give",
    "list",
    "main"
}


# =========================================================
# QUERY EXPANSION
# =========================================================

QUERY_EXPANSIONS = {
    "objective": {
        "objective",
        "objectives",
        "aim",
        "aims",
        "goal",
        "goals",
        "purpose"
    },

    "guide": {
        "guide",
        "supervisor",
        "mentor",
        "faculty",
        "advisor",
        "adviser"
    },

    "problem": {
        "problem",
        "problems",
        "statement",
        "challenge",
        "issue"
    },

    "technology": {
        "technology",
        "technologies",
        "tools",
        "software",
        "framework",
        "frameworks",
        "tech",
        "stack"
    },

    "scope": {
        "scope",
        "future",
        "enhancement",
        "enhancements",
        "improvement",
        "improvements"
    },

    "conclusion": {
        "conclusion",
        "conclusions",
        "result",
        "results",
        "finding",
        "findings"
    }
}


def extract_keywords(text):

    words = normalize_text(text).split()

    keywords = {
        word
        for word in words
        if word not in STOP_WORDS
        and len(word) >= 3
    }

    expanded = set(keywords)

    for word in keywords:

        for canonical, synonyms in QUERY_EXPANSIONS.items():

            if word in synonyms:
                expanded.update(synonyms)

    return expanded


# =========================================================
# SECTION-AWARE KEYWORD BOOST
# =========================================================

def section_keyword_boost(
    question,
    document
):

    question_text = normalize_text(question)
    document_text = normalize_text(document)

    score = 0.0

    # Objectives
    if any(
        term in question_text
        for term in [
            "objective",
            "objectives",
            "aim",
            "aims",
            "goal",
            "goals",
            "purpose"
        ]
    ):

        if any(
            term in document_text
            for term in [
                "objective",
                "objectives",
                "aim",
                "aims",
                "goal",
                "goals",
                "purpose"
            ]
        ):
            score = max(score, 0.85)


    # Project guide
    if (
        "guide" in question_text
        or "supervisor" in question_text
        or "mentor" in question_text
    ):

        if any(
            term in document_text
            for term in [
                "guide",
                "supervisor",
                "mentor",
                "faculty",
                "advisor",
                "adviser"
            ]
        ):
            score = max(score, 0.85)


    # Problem statement
    if (
        "problem" in question_text
        or "statement" in question_text
        or "challenge" in question_text
    ):

        if any(
            term in document_text
            for term in [
                "problem",
                "statement",
                "challenge"
            ]
        ):
            score = max(score, 0.85)


    # Technologies
    if (
        "technology" in question_text
        or "technologies" in question_text
        or "tools" in question_text
        or "framework" in question_text
        or "used" in question_text
    ):

        if any(
            term in document_text
            for term in [
                "technology",
                "technologies",
                "tools",
                "framework",
                "python",
                "software"
            ]
        ):
            score = max(score, 0.80)


    return score


# =========================================================
# LEXICAL SCORE
# =========================================================

def lexical_score(
    question,
    document
):

    question_normalized = normalize_text(
        question
    )

    document_normalized = normalize_text(
        document
    )

    question_keywords = extract_keywords(
        question
    )

    document_keywords = extract_keywords(
        document
    )

    if not question_keywords:
        return 0.0

    overlap = (
        question_keywords
        & document_keywords
    )

    overlap_score = (
        len(overlap)
        / max(len(question_keywords), 1)
    )

    phrase_score = 0.0

    if (
        question_normalized
        in document_normalized
        and len(question_normalized) >= 5
    ):
        phrase_score = 1.0


    section_score = section_keyword_boost(
        question,
        document
    )


    return min(
        1.0,
        (
            overlap_score * 0.45
            +
            phrase_score * 0.20
            +
            section_score * 0.35
        )
    )


# =========================================================
# RETRIEVAL
# =========================================================

def retrieve_relevant_chunks(
    collection,
    embedding_model,
    question
):

    question_embedding = (
        embedding_model.encode(
            [question],
            normalize_embeddings=True,
            show_progress_bar=False
        )[0]
    )


    results = collection.query(
        query_embeddings=[
            question_embedding.tolist()
        ],
        n_results=12,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )


    documents = (
        results.get("documents", [[]])[0]
    )

    metadatas = (
        results.get("metadatas", [[]])[0]
    )

    distances = (
        results.get("distances", [[]])[0]
    )


    candidates = []


    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):

        # Chroma cosine distance is normally
        # lower = better.
        #
        # Convert it into a similarity-like
        # score while keeping it between 0 and 1.

        distance_value = float(distance)

        semantic_score = max(
            0.0,
            min(
                1.0,
                1.0 - distance_value
            )
        )


        keyword_score = lexical_score(
            question,
            document
        )


        # Extra boost when important section
        # terminology appears in the chunk.

        section_score = section_keyword_boost(
            question,
            document
        )


        final_score = (
            semantic_score * 0.50
            +
            keyword_score * 0.30
            +
            section_score * 0.20
        )


        candidates.append({
            "document": document,
            "metadata": metadata,
            "distance": distance_value,
            "semantic_score": semantic_score,
            "keyword_score": keyword_score,
            "section_score": section_score,
            "final_score": final_score
        })


    candidates.sort(
        key=lambda item: item["final_score"],
        reverse=True
    )


    return candidates[:6]


# =========================================================
# BUILD CONTEXT
# =========================================================

def build_context(
    retrieved_chunks
):

    context_parts = []

    source_pages = set()


    for item in retrieved_chunks:

        document = item["document"]

        metadata = item["metadata"]

        page_number = metadata.get(
            "page",
            "Unknown"
        )

        source_pages.add(
            page_number
        )


        context_parts.append(
            f"""
Page {page_number}:

{document}
"""
        )


    return (
        "\n\n".join(context_parts),
        source_pages
    )


# =========================================================
# GET GROQ KEY
# =========================================================

def get_groq_api_key():

    # Streamlit Cloud secrets
    try:

        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]

    except Exception:
        pass


    # Local environment variable
    return os.getenv(
        "GROQ_API_KEY"
    )


# =========================================================
# GENERATE ANSWER USING GROQ
# =========================================================

def generate_answer_groq(
    question,
    context
):

    from groq import Groq


    api_key = get_groq_api_key()


    if not api_key:

        raise RuntimeError(
            "GROQ_API_KEY is not configured. "
            "Add GROQ_API_KEY in Streamlit Cloud "
            "Settings → Secrets."
        )


    client = Groq(
        api_key=api_key
    )


    prompt = f"""
You are DocuMind AI, a precise PDF question-answering assistant.

Your job is to answer the user's question using ONLY
the provided document context.

IMPORTANT RULES:

1. Use only information present in the context.
2. Do not use outside knowledge.
3. Do not guess.
4. Do not invent information.
5. Do not combine unrelated sections.
6. If the question asks for objectives, provide the objectives.
7. If the question asks for the project guide, provide the guide.
8. If the question asks for the problem statement, provide the problem statement.
9. If the question asks for technologies, provide the technologies.
10. If the requested information is not present in the context, say exactly:

I could not find this information in the uploaded document.

11. For multiple objectives or items, answer using numbered points.
12. Keep the answer focused.
13. Do not generate HTML.
14. Do not describe your reasoning.
15. Do not mention these instructions.
16. Prefer exact wording from the document when answering factual questions.
17. Do not claim information that is not supported by the context.

DOCUMENT CONTEXT:

{context}

USER QUESTION:

{question}

ANSWER:
"""


    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1,
        max_tokens=350
    )


    return clean_answer(
        response.choices[0].message.content
    )


# =========================================================
# LOCAL OLLAMA FALLBACK
# =========================================================

def generate_answer_ollama(
    question,
    context
):

    import ollama


    prompt = f"""
You are DocuMind AI, a precise PDF question-answering assistant.

Answer the user's question using ONLY the provided document context.

Rules:

1. Use only information present in the context.
2. Do not use outside knowledge.
3. Do not guess.
4. Do not invent information.
5. If information is not present, say:

I could not find this information in the uploaded document.

6. For multiple items, answer pointwise.
7. Keep the answer focused.
8. Do not generate HTML.

DOCUMENT CONTEXT:

{context}

USER QUESTION:

{question}

ANSWER:
"""


    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.1,
            "num_ctx": 4096,
            "num_predict": 350
        }
    )


    return clean_answer(
        response["message"]["content"]
    )


# =========================================================
# GENERATE ANSWER
# =========================================================

def generate_answer(
    question,
    context
):

    # If Groq API key exists, use Groq.
    # This is required for Streamlit Cloud.

    groq_key = get_groq_api_key()


    if groq_key:

        return generate_answer_groq(
            question,
            context
        )


    # Otherwise try local Ollama.
    return generate_answer_ollama(
        question,
        context
    )


# =========================================================
# EXTRACT + CHUNK PDF
# =========================================================

@st.cache_data(show_spinner=False)
def extract_and_chunk_pdf(
    pdf_bytes,
    source_name
):

    from pypdf import PdfReader

    from langchain_text_splitters import (
        RecursiveCharacterTextSplitter
    )


    reader = PdfReader(
        io.BytesIO(pdf_bytes)
    )


    pages_data = []


    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        text = page.extract_text()


        if text and text.strip():

            cleaned_text = re.sub(
                r"[ \t]+",
                " ",
                text
            )

            cleaned_text = re.sub(
                r"\n{3,}",
                "\n\n",
                cleaned_text
            )


            pages_data.append({
                "page": page_number,
                "text": cleaned_text.strip()
            })


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=650,
        chunk_overlap=100,
        separators=[
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            " ",
            ""
        ]
    )


    chunks = []


    for page_data in pages_data:

        page_chunks = splitter.split_text(
            page_data["text"]
        )


        for chunk_index, chunk in enumerate(
            page_chunks
        ):

            if not chunk.strip():
                continue


            chunks.append({
                "text": chunk.strip(),
                "page": page_data["page"],
                "source": source_name,
                "chunk_index": chunk_index
            })


    return pages_data, chunks


# =========================================================
# CREATE EMBEDDINGS
# =========================================================

@st.cache_data(show_spinner=False)
def create_document_embeddings(
    pdf_hash,
    texts
):

    embedding_model = (
        load_embedding_model()
    )


    return embedding_model.encode(
        list(texts),
        batch_size=64,
        normalize_embeddings=True,
        show_progress_bar=False
    )


# =========================================================
# PROCESS PDF
# =========================================================

def process_pdf(
    uploaded_file
):

    pdf_bytes = uploaded_file.getvalue()


    pdf_hash = hashlib.md5(
        pdf_bytes
    ).hexdigest()


    if (
        st.session_state.processed_pdf_hash
        == pdf_hash
        and st.session_state.document_ready
    ):
        return


    chroma_client = (
        get_chroma_client()
    )


    pages_data, chunks = (
        extract_and_chunk_pdf(
            pdf_bytes,
            uploaded_file.name
        )
    )


    collection_name = (
        f"pdf_{pdf_hash}"
    )


    collection = (
        chroma_client.get_or_create_collection(
            name=collection_name
        )
    )


    existing_count = (
        collection.count()
    )


    if existing_count == 0 and chunks:

        texts = tuple(
            chunk["text"]
            for chunk in chunks
        )


        embeddings = (
            create_document_embeddings(
                pdf_hash,
                texts
            )
        )


        ids = [
            f"{pdf_hash}_{i}"
            for i in range(len(chunks))
        ]


        documents = [
            chunk["text"]
            for chunk in chunks
        ]


        metadatas = [
            {
                "page": chunk["page"],
                "source": chunk["source"],
                "chunk_index": chunk["chunk_index"]
            }
            for chunk in chunks
        ]


        collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )


    st.session_state.processed_pdf_hash = (
        pdf_hash
    )

    st.session_state.pages_data = (
        pages_data
    )

    st.session_state.chunks = (
        chunks
    )

    st.session_state.collection_name = (
        collection_name
    )

    st.session_state.collection = (
        collection
    )

    st.session_state.document_name = (
        uploaded_file.name
    )

    st.session_state.embedding_dimension = 384

    st.session_state.document_ready = True

    st.session_state.chat_history = []


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
<div class="sidebar-brand">
    <span class="sidebar-brand-icon">✦</span>
    DocuMind AI
</div>

<div class="sidebar-description">
    Private document intelligence
</div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="sidebar-heading">SYSTEM</div>',
        unsafe_allow_html=True
    )


    groq_available = bool(
        get_groq_api_key()
    )


    if groq_available:

        llm_name = "Groq Llama 3.1 8B"

        llm_status = "Cloud LLM ready"

    else:

        llm_name = "Ollama Llama 3.2"

        llm_status = "Local LLM mode"


    st.markdown(
        f"""
<div class="sidebar-card">

    <div class="sidebar-status">
        <span class="status-dot"></span>
        {llm_status}
    </div>

    <br>

    <strong>LLM</strong><br>
    {llm_name}

    <br><br>

    <strong>Embeddings</strong><br>
    all-MiniLM-L6-v2

    <br><br>

    <strong>Vector Database</strong><br>
    ChromaDB

    <br><br>

    <strong>Architecture</strong><br>
    Retrieval-Augmented Generation

</div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="sidebar-heading">PERFORMANCE</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        """
<div class="sidebar-card">

    ⚡ Cached model loading

    <br><br>

    🎯 Semantic + keyword reranking

    <br><br>

    📦 Multi-chunk context

    <br><br>

    🧠 Low-temperature generation

</div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="sidebar-heading">ARCHITECTURE</div>',
        unsafe_allow_html=True
    )


    if groq_available:

        privacy_text = """
<div class="sidebar-card">

    🔐 Local PDF processing and embeddings.

    <br><br>

    Retrieved context is sent to the
    configured Groq LLM for answer generation.

</div>
        """

    else:

        privacy_text = """
<div class="sidebar-card">

    🔒 Local processing mode.

    <br><br>

    No cloud LLM configured.
    Local Ollama inference is used.

</div>
        """


    st.markdown(
        privacy_text,
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="sidebar-heading">DOCUMENT</div>',
        unsafe_allow_html=True
    )


    if st.session_state.document_name:

        st.markdown(
            f"""
<div class="sidebar-card">

    <strong>
        {st.session_state.document_name}
    </strong>

    <br><br>

    {len(st.session_state.pages_data)}
    pages

    &nbsp;•&nbsp;

    {len(st.session_state.chunks)}
    chunks

</div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
<div class="sidebar-card">
    No document loaded yet.
</div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("")


    if st.button(
        "＋  New Document",
        use_container_width=True
    ):

        st.session_state.processed_pdf_hash = None
        st.session_state.pages_data = []
        st.session_state.chunks = []
        st.session_state.collection_name = None
        st.session_state.collection = None
        st.session_state.document_name = None
        st.session_state.chat_history = []
        st.session_state.document_ready = False

        st.rerun()


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
<div class="hero">

    <div class="hero-symbol">
        ✦
    </div>

    <div class="hero-title">
        DocuMind AI
    </div>

    <div class="hero-subtitle">
        Ask questions. Find answers. Stay private.
    </div>

</div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# UPLOAD
# =========================================================

st.markdown(
    '<div class="upload-title">DOCUMENT</div>',
    unsafe_allow_html=True
)


uploaded_file = st.file_uploader(
    "📎 Upload a PDF",
    type=["pdf"],
    help="Upload a PDF document to start chatting with it."
)


# =========================================================
# PROCESS PDF
# =========================================================

if uploaded_file is not None:

    pdf_bytes = uploaded_file.getvalue()


    pdf_hash = hashlib.md5(
        pdf_bytes
    ).hexdigest()


    if (
        st.session_state.processed_pdf_hash
        != pdf_hash
    ):

        with st.status(
            "Preparing your document...",
            expanded=False
        ) as status:

            try:

                process_pdf(
                    uploaded_file
                )


                status.update(
                    label="Document ready",
                    state="complete"
                )


            except Exception as error:

                status.update(
                    label="Document processing failed",
                    state="error"
                )


                st.error(
                    f"Could not process the PDF: {error}"
                )

                st.stop()


# =========================================================
# DOCUMENT READY
# =========================================================

if st.session_state.document_ready:

    pages_count = len(
        st.session_state.pages_data
    )


    chunks_count = len(
        st.session_state.chunks
    )


    # -----------------------------------------------------
    # DOCUMENT BAR
    # -----------------------------------------------------

    st.markdown(
        f"""
<div class="document-bar">

    <div class="document-icon">
        📄
    </div>

    <div>

        <div class="document-name">
            {st.session_state.document_name}
        </div>

        <div class="document-meta">
            {pages_count} pages
            &nbsp;•&nbsp;
            {chunks_count} chunks
            &nbsp;•&nbsp;
            384-dimensional embeddings
            &nbsp;•&nbsp;
            RAG
        </div>

    </div>

</div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # WELCOME
    # -----------------------------------------------------

    if not st.session_state.chat_history:

        st.markdown(
            """
<div class="welcome">

    <div class="welcome-title">
        Your document is ready.
    </div>

    <div class="welcome-text">
        Ask a question and DocuMind will
        retrieve the most relevant information
        from your PDF.
    </div>

</div>
            """,
            unsafe_allow_html=True
        )


        col1, col2 = st.columns(2)


        with col1:

            st.markdown(
                """
<div class="suggestion-box">
    💡 What are the main objectives?
</div>
                """,
                unsafe_allow_html=True
            )


            st.markdown(
                """
<div class="suggestion-box">
    💡 Summarize the document.
</div>
                """,
                unsafe_allow_html=True
            )


        with col2:

            st.markdown(
                """
<div class="suggestion-box">
    💡 Who is the project guide?
</div>
                """,
                unsafe_allow_html=True
            )


            st.markdown(
                """
<div class="suggestion-box">
    💡 What is the problem statement?
</div>
                """,
                unsafe_allow_html=True
            )


    # =====================================================
    # CHAT HISTORY
    # =====================================================

    for message in st.session_state.chat_history:

        if message["role"] == "user":

            with st.chat_message("user"):

                st.markdown(
                    message["content"]
                )


        else:

            with st.chat_message("assistant"):

                st.markdown(
                    message["content"]
                )


                if message.get("sources"):

                    st.markdown(
                        '<div class="source-label">'
                        'Sources'
                        '</div>',
                        unsafe_allow_html=True
                    )


                    source_html = ""


                    for page in message["sources"]:

                        source_html += (
                            f'<span class="source-pill">'
                            f'📄 Page {page}'
                            f'</span>'
                        )


                    st.markdown(
                        source_html,
                        unsafe_allow_html=True
                    )


    # =====================================================
    # CHAT INPUT
    # =====================================================

    question = st.chat_input(
        "Ask your document anything..."
    )


    if question:

        st.session_state.chat_history.append({
            "role": "user",
            "content": question
        })


        try:

            embedding_model = (
                load_embedding_model()
            )


            with st.spinner(
                "✦ Finding the most relevant information..."
            ):

                retrieved_chunks = (
                    retrieve_relevant_chunks(
                        st.session_state.collection,
                        embedding_model,
                        question
                    )
                )


            context, source_pages = (
                build_context(
                    retrieved_chunks
                )
            )


            if not retrieved_chunks:

                answer = (
                    "I could not find this information "
                    "in the uploaded document."
                )

                source_pages = set()


            else:

                best_score = (
                    retrieved_chunks[0]["final_score"]
                )

                best_keyword_score = (
                    retrieved_chunks[0]["keyword_score"]
                )


                # More permissive than the previous
                # 0.18-only threshold.
                #
                # A strong keyword/section match is
                # allowed even when semantic similarity
                # is not extremely high.

                information_found = (
                    best_score >= 0.10
                    or best_keyword_score >= 0.20
                )


                if not information_found:

                    answer = (
                        "I could not find this information "
                        "in the uploaded document."
                    )

                    source_pages = set()


                else:

                    with st.spinner(
                        "✦ Generating answer..."
                    ):

                        try:

                            answer = generate_answer(
                                question,
                                context
                            )

                        except Exception as llm_error:

                            answer = (
                                "The document was retrieved "
                                "successfully, but the answer "
                                "generation service is not "
                                "configured correctly.\n\n"
                                f"Details: {llm_error}"
                            )


            st.session_state.chat_history.append({
                "role": "assistant",
                "content": answer,
                "sources": sorted(
                    source_pages
                )
            })


            st.rerun()


        except Exception as error:

            st.session_state.chat_history.append({
                "role": "assistant",
                "content": (
                    "I encountered an error while "
                    f"processing your question: {error}"
                ),
                "sources": []
            })


            st.rerun()


    # =====================================================
    # RETRIEVAL DEBUGGER
    # =====================================================

    with st.expander(
        "🔎  View Retrieved Context"
    ):

        st.caption(
            "Inspect the chunks selected by the "
            "semantic + keyword retrieval system."
        )


        debug_question = st.text_input(
            "Test retrieval",
            placeholder="Enter a question..."
        )


        if debug_question:

            try:

                embedding_model = (
                    load_embedding_model()
                )


                debug_chunks = (
                    retrieve_relevant_chunks(
                        st.session_state.collection,
                        embedding_model,
                        debug_question
                    )
                )


                if not debug_chunks:

                    st.warning(
                        "No relevant chunks were retrieved."
                    )


                for i, item in enumerate(
                    debug_chunks,
                    start=1
                ):

                    metadata = item["metadata"]


                    st.markdown(
                        f"**Result {i} — "
                        f"Page {metadata['page']}**"
                    )


                    st.caption(
                        f"Final score: "
                        f"{item['final_score']:.3f}"
                        f"  •  "
                        f"Semantic: "
                        f"{item['semantic_score']:.3f}"
                        f"  •  "
                        f"Keyword: "
                        f"{item['keyword_score']:.3f}"
                        f"  •  "
                        f"Section: "
                        f"{item['section_score']:.3f}"
                        f"  •  "
                        f"Distance: "
                        f"{item['distance']:.3f}"
                    )


                    st.write(
                        item["document"]
                    )


                    st.divider()


            except Exception as error:

                st.error(
                    f"Retrieval test failed: {error}"
                )


# =========================================================
# EMPTY STATE
# =========================================================

else:

    st.markdown(
        """
<div class="welcome">

    <div class="welcome-title">
        Your documents, made searchable.
    </div>

    <div class="welcome-text">

        Upload a PDF and start asking questions.

        <br><br>

        <strong>
            Local Embeddings
        </strong>
        &nbsp; • &nbsp;

        <strong>
            ChromaDB
        </strong>
        &nbsp; • &nbsp;

        <strong>
            RAG
        </strong>
        &nbsp; • &nbsp;

        <strong>
            Llama 3.2
        </strong>

    </div>

</div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
<div class="footer">

    ✦ DocuMind AI
    &nbsp;•&nbsp;
    Local RAG
    &nbsp;•&nbsp;
    Private by design

</div>
    """,
    unsafe_allow_html=True
)