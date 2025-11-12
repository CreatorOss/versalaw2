"""
Maya Legal AI - Example Usage
"""

import sys
import os

# Add to path
sys.path.insert(0, 'src')

def main():
    print("🔮 Maya Legal AI - Example Usage")
    print("=" * 40)
    
    try:
        from versalaw2 import MayaLegalQASystem, MayaWisdomProcessor
        from versalaw2 import EnhancedLegalAnalyzer, ContractAnalyzer
        
        # Initialize systems
        qa_system = MayaLegalQASystem()
        wisdom_system = MayaWisdomProcessor()
        analyzer = EnhancedLegalAnalyzer()
        contract_analyzer = ContractAnalyzer()
        
        print("✅ Systems initialized successfully!")
        print()
        
        # Example questions
        questions = [
            "What are the requirements for a valid contract in Indonesia?",
            "Explain data protection laws for businesses",
            "What is the legal status of electronic signatures?"
        ]
        
        for i, question in enumerate(questions, 1):
            print(f"{i}. ❓ {question}")
            
            # Get answer from QA system
            answer = qa_system.ask(question)
            print(f"   ✅ Answer: {answer.answer[:100]}...")
            print(f"   🎯 Confidence: {answer.confidence:.0%}")
            
            # Get wisdom insights
            wisdom = wisdom_system.process_legal_query(question)
            print(f"   🔮 Wisdom: {wisdom['analysis']}")
            
            # Analyze as document
            analysis = analyzer.analyze_document(question)
            print(f"   🔍 Analysis: {analysis['analysis_summary']}")
            
            print()
        
        print("🎉 Example completed successfully!")
        print("Maya Legal AI is ready for your applications!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
