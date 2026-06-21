import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("AI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")


def analyze_sentiment(comment: str):
    try:
        response = model.generate_content(
            f"""
            Определи тональность сообщения.
            Ответь только одним словом:
            positive, negative или neutral

            Сообщение:
            {comment}
            """
        )

        return response.text.strip()

    except Exception as e:
        # print("AI ERROR:", e)

        positive_words = [
            "спасибо",
            "благодарю",
            "отлично",
            "супер",
            "круто",
            "классно",
            "замечательно",
            "прекрасно",
            "великолепно",
            "хорошо",
            "понравилось",
            "доволен",
            "довольна",
            "рекомендую",
            "лучший",
            "лучшее",
            "awesome",
            "great",
            "perfect",
            "excellent",
            "good",
            "amazing",
            "love",
            "fantastic"
        ]

        negative_words = [
            "ужасно",
            "отстой",
            "плохо",
            "ненавижу",
            "отвратительно",
            "кошмар",
            "безобразно",
            "ужасный",
            "ужасная",
            "разочарован",
            "разочарована",
            "не понравилось",
            "худший",
            "худшее",
            "мерзко",
            "провал",
            "bad",
            "terrible",
            "awful",
            "hate",
            "worst",
            "disgusting",
            "poor"
        ]

        text = comment.lower()

        if any(word in text for word in positive_words):
            return "positive"

        if any(word in text for word in negative_words):
            return "negative"

        return "neutral"