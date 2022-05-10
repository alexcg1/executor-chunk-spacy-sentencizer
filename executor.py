from jina import Executor, requests


class ChunkSpacySentencizer(Executor):
    """
    Sentencizes a Document's chunks with SpacySentencizer
    """

    @requests(on="/index")
    def sentencize_text_chunks(self, docs, **kwargs):
        sentencizer_name = "jinahub://SpacySentencizer/v0.4"
        for doc in docs:
            sentencizer = Executor.from_hub(
                sentencizer_name,
                install_requirements=True,
            )
            sentencizer.segment(doc.chunks, parameters={})
