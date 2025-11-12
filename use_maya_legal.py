"""
Maya Legal AI - Simple Usage Template
Copy this template for your projects!
"""

import sys
import os

# Setup path - CHANGE THIS to your actual path
sys.path.insert(0, '/root/dragon/global/versalaw2/src')

def ask_legal_question(question):
    """
    Ask a legal question to Maya Legal AI
    """
    try:
        from versalaw2 import MayaLegalQASystem, MayaWisdomProcessor
        
        # Initialize systems
        qa_system = MayaLegalQASystem()
        wisdom_system = MayaWisdomProcessor()
        
        # Get answers
        legal_answer = qa_system.ask(question)
        wisdom_insights = wisdom_system.process_legal_query(question)
        
        return {
            'question': question,
            'answer': legal_answer.answer,
            'confidence': legal_answer.confidence,
            'sources': legal_answer.sources,
            'wisdom': wisdom_insights['analysis']
        }
        
    except Exception as e:
        return {'error': str(e)}

# Example usage
if __name__ == "__main__":
    questions = [
        "What are the requirements for a valid contract?",
        "Explain data protection laws",
        "What is copyright law?"
    ]
    
    for q in questions:
        result = ask_legal_question(q)
        if 'error' not in result:
            print(f"❓ {result['question']}")
            print(f"✅ {result['answer'][:100]}...")
            print(f"🎯 Confidence: {result['confidence']:.0%}")
            print(f"🔮 Wisdom: {result['wisdom']}")
            print("-" * 50)
        else:
            print(f"❌ Error: {result['error']}")
