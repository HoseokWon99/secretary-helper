from ProofDocumentGenerator import ProofDocumentGenerator

if __name__ == '__main__':
    generator = ProofDocumentGenerator(2024, 2)

    generator.generate(
        "영수증",
        "/Users/hoseok/Desktop/증빙자료",
        "/Users/hoseok/Desktop"
    )