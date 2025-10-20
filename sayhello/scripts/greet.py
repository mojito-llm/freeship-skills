#!/usr/bin/env python3
"""
Greeting Generator Script

Generate contextual greetings in multiple languages and styles.

Usage:
    python greet.py --language chinese --style formal
    python greet.py --style casual --time morning
    python greet.py --language spanish --context business
"""

import argparse
import sys
from datetime import datetime
from typing import Dict, List, Tuple


class GreetingGenerator:
    """Generate greetings based on language, style, context, and time."""

    GREETINGS: Dict[str, Dict[str, List[str]]] = {
        "english": {
            "formal": [
                "Good day",
                "Greetings",
                "I hope this message finds you well"
            ],
            "casual": [
                "Hey",
                "Hi there",
                "Hello",
                "What's up"
            ],
            "professional": [
                "Good morning/afternoon",
                "Hello",
                "Dear [Name]"
            ]
        },
        "chinese": {
            "formal": [
                "您好 (nín hǎo)",
                "尊敬的 [Name] (zūn jìng de)",
                "很高兴见到您 (hěn gāo xìng jiàn dào nín)"
            ],
            "casual": [
                "你好 (nǐ hǎo)",
                "嗨 (hāi)",
                "哈喽 (hā lou)"
            ],
            "professional": [
                "您好 (nín hǎo)",
                "早上好 (zǎo shang hǎo)",
                "下午好 (xià wǔ hǎo)"
            ]
        },
        "spanish": {
            "formal": [
                "Buenos días (bweh-nos DEE-ahs)",
                "Estimado/a [Name]",
                "Es un placer conocerle"
            ],
            "casual": [
                "¡Hola! (OH-lah)",
                "¿Qué tal?",
                "¡Buenas!"
            ],
            "professional": [
                "Buenos días",
                "Buenas tardes",
                "Hola, [Name]"
            ]
        },
        "japanese": {
            "formal": [
                "おはようございます (ohayō gozaimasu)",
                "こんにちは (konnichiwa)",
                "お会いできて光栄です (o-ai dekite kōei desu)"
            ],
            "casual": [
                "やあ (yā)",
                "おっす (ossu)",
                "こんちは (konchiwa)"
            ],
            "professional": [
                "おはようございます (ohayō gozaimasu)",
                "こんにちは (konnichiwa)",
                "[Name]さん、お疲れ様です"
            ]
        },
        "french": {
            "formal": [
                "Bonjour (bon-ZHOOR)",
                "Enchanté(e)",
                "Ravi(e) de vous rencontrer"
            ],
            "casual": [
                "Salut (sa-LOO)",
                "Coucou",
                "Ça va?"
            ],
            "professional": [
                "Bonjour",
                "Bonsoir",
                "Madame/Monsieur [Name]"
            ]
        }
    }

    TIME_GREETINGS: Dict[str, Dict[str, str]] = {
        "morning": {
            "english": "Good morning",
            "chinese": "早上好 (zǎo shang hǎo)",
            "spanish": "Buenos días",
            "japanese": "おはようございます (ohayō gozaimasu)",
            "french": "Bonjour"
        },
        "afternoon": {
            "english": "Good afternoon",
            "chinese": "下午好 (xià wǔ hǎo)",
            "spanish": "Buenas tardes",
            "japanese": "こんにちは (konnichiwa)",
            "french": "Bon après-midi"
        },
        "evening": {
            "english": "Good evening",
            "chinese": "晚上好 (wǎn shang hǎo)",
            "spanish": "Buenas noches",
            "japanese": "こんばんは (konbanwa)",
            "french": "Bonsoir"
        },
        "night": {
            "english": "Good night",
            "chinese": "晚安 (wǎn ān)",
            "spanish": "Buenas noches",
            "japanese": "おやすみなさい (oyasuminasai)",
            "french": "Bonne nuit"
        }
    }

    CONTEXT_TEMPLATES: Dict[str, str] = {
        "business": """Dear [Name],

{greeting}

I hope this message finds you well. I am reaching out to discuss...

Best regards,
[Your Name]""",

        "email": """Hello [Name],

{greeting}

I wanted to reach out regarding...

Kind regards,
[Your Name]""",

        "social": """{greeting}

Great to connect with you!

Cheers,
[Your Name]""",

        "meeting": """{greeting}

Thank you for taking the time to meet with me today.

Looking forward to our discussion.

Best,
[Your Name]"""
    }

    def __init__(self):
        self.current_hour = datetime.now().hour

    def get_auto_time(self) -> str:
        """Automatically determine time of day based on current hour."""
        if 5 <= self.current_hour < 12:
            return "morning"
        elif 12 <= self.current_hour < 17:
            return "afternoon"
        elif 17 <= self.current_hour < 21:
            return "evening"
        else:
            return "night"

    def generate(
        self,
        language: str = "english",
        style: str = "casual",
        context: str = None,
        time: str = None
    ) -> str:
        """
        Generate a greeting based on parameters.

        Args:
            language: Target language
            style: Formality level (formal/casual/professional)
            context: Specific context (business/email/social/meeting)
            time: Time of day (morning/afternoon/evening/night)

        Returns:
            Generated greeting string
        """
        language = language.lower()
        style = style.lower()

        # Validate inputs
        if language not in self.GREETINGS:
            available = ", ".join(self.GREETINGS.keys())
            return f"Error: Language '{language}' not supported. Available: {available}"

        if style not in self.GREETINGS[language]:
            available = ", ".join(self.GREETINGS[language].keys())
            return f"Error: Style '{style}' not available. Available: {available}"

        # Generate greeting based on time if specified
        if time:
            time = time.lower()
            if time in self.TIME_GREETINGS:
                greeting = self.TIME_GREETINGS[time].get(language, "Hello")
            else:
                greeting = self.GREETINGS[language][style][0]
        else:
            # Use first greeting from the style list
            greeting = self.GREETINGS[language][style][0]

        # Apply context template if specified
        if context and context.lower() in self.CONTEXT_TEMPLATES:
            template = self.CONTEXT_TEMPLATES[context.lower()]
            return template.format(greeting=greeting)

        return greeting

    def list_options(self) -> str:
        """List all available languages, styles, and contexts."""
        output = []
        output.append("Available Languages:")
        for lang in self.GREETINGS.keys():
            output.append(f"  - {lang}")

        output.append("\nAvailable Styles:")
        output.append("  - formal")
        output.append("  - casual")
        output.append("  - professional")

        output.append("\nAvailable Contexts:")
        for ctx in self.CONTEXT_TEMPLATES.keys():
            output.append(f"  - {ctx}")

        output.append("\nAvailable Times:")
        for t in self.TIME_GREETINGS.keys():
            output.append(f"  - {t}")

        return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Generate contextual greetings in multiple languages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python greet.py --language chinese --style formal
  python greet.py --style casual --time morning
  python greet.py --language spanish --context business
  python greet.py --list
        """
    )

    parser.add_argument(
        "--language",
        default="english",
        help="Target language (default: english)"
    )
    parser.add_argument(
        "--style",
        default="casual",
        help="Formality level: formal, casual, professional (default: casual)"
    )
    parser.add_argument(
        "--context",
        help="Specific context: business, email, social, meeting"
    )
    parser.add_argument(
        "--time",
        help="Time of day: morning, afternoon, evening, night"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available options"
    )

    args = parser.parse_args()

    generator = GreetingGenerator()

    if args.list:
        print(generator.list_options())
        return 0

    greeting = generator.generate(
        language=args.language,
        style=args.style,
        context=args.context,
        time=args.time
    )

    print(greeting)
    return 0


if __name__ == "__main__":
    sys.exit(main())
