# ChunkSpacySentencizer

Sentencizes a Document's chunks with [SpacySentencizer](https://hub.jina.ai/executor/197kj4fv)

## Usage

#### via Docker image (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://ChunkSpacySentencizer')
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://ChunkSpacySentencizer')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`
