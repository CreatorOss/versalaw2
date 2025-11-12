from versalaw2 import MayaLegalQASystem

# Initialize the system
qa_system = MayaLegalQASystem()

# Ask legal questions
question = "What are the requirements for a valid contract in Indonesia?"
answer = qa_system.ask(question)

print(f"📖 Answer: {answer.answer}")
print(f"🎯 Confidence: {answer.confidence:.0%}")
print(f"📚 Sources: {', '.join(answer.sources)}")
