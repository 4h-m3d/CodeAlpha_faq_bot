import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load English tokenizer
nlp = spacy.load("en_core_web_sm")

# Example FAQs
faqs = {
    "What is your return policy?": "You can return any product within 30 days of purchase.",
    "How long does delivery take?": "Delivery typically takes 3–5 business days.",
    "Do you ship internationally?": "Yes, we offer international shipping to selected countries.",
    "What payment methods do you accept?": "We accept Visa, MasterCard, PayPal, and Apple Pay.",
    "How can I track my order?": "You will receive a tracking link via email once your order is shipped.",

    # New FAQs
    "Can I change my order after placing it?": "Yes, you can change your order within 24 hours of placing it by contacting customer support.",
    "Do you offer discounts for bulk purchases?": "Yes, we offer discounts for orders above $500. Contact our sales team for details.",
    "What should I do if I receive a damaged item?": "Please contact our support team within 7 days, and we’ll replace the item or issue a refund.",
    "Do you have a physical store?": "Currently, we are an online-only store.",
    "Which courier services do you use?": "We primarily ship using FedEx and DHL for fast delivery."
}

# Preprocessing function
def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])

# Prepare data
questions = list(faqs.keys())
processed_questions = [preprocess(q) for q in questions]

# TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_questions)

# Matching function
def get_response(user_input):
    user_input_processed = preprocess(user_input)
    user_vec = vectorizer.transform([user_input_processed])
    similarities = cosine_similarity(user_vec, tfidf_matrix)
    best_match_idx = similarities.argmax()
    best_score = similarities[0][best_match_idx]

    if best_score < 0.3:
        return "Sorry, I couldn't find an answer to that."

    return faqs[questions[best_match_idx]]

# CLI loop
def run_chat():
    print("FAQ Chatbot is ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        print("Bot:", get_response(user_input))

if __name__ == "__main__":
    run_chat()
