# spaCy 词性标签（POS Tags）和依存关系标签（Dependency Labels）

本文档汇总了 spaCy 中使用的所有可能的词性标签和依存关系标签，供参考。

## 词性标签（`Token.pos_`）

spaCy 使用了通用词性标签（Universal POS Tags），以下是完整列表：

- **ADJ**：形容词
- **ADP**：介词或后置词
- **ADV**：副词
- **AUX**：助动词
- **CONJ**：连词
- **CCONJ**：并列连词
- **DET**：限定词
- **INTJ**：感叹词
- **NOUN**：名词
- **NUM**：数词
- **PART**：小品词
- **PRON**：代词
- **PROPN**：专有名词
- **PUNCT**：标点符号
- **SCONJ**：从属连词
- **SYM**：符号
- **VERB**：动词
- **X**：其他

## 依存关系标签（`Token.dep_`）

spaCy 使用了基于 Universal Dependencies 的依存关系标签，以下是可能的标签列表：

- **acl**：限定性从句修饰语
- **acomp**：表语补足语
- **advcl**：状语从句
- **advmod**：状语修饰语
- **agent**：施事
- **amod**：形容词修饰语
- **appos**：同位语
- **attr**：表语
- **aux**：助动词
- **auxpass**：被动助动词
- **case**：格标记
- **cc**：并列连词
- **ccomp**：补语从句
- **compound**：复合词
- **conj**：并列结构
- **cop**：系动词
- **csubj**：从句主语
- **csubjpass**：被动从句主语
- **dative**：与格
- **dep**：未标注的依存关系
- **det**：限定词
- **dobj**：直接宾语
- **expl**：存在词
- **intj**：感叹词
- **mark**：从属连词
- **meta**：元数据
- **neg**：否定词
- **nmod**：名词修饰语
- **npadvmod**：名词短语状语修饰语
- **nsubj**：名词主语
- **nsubjpass**：被动名词主语
- **nummod**：数词修饰语
- **oprd**：宾语补足语
- **parataxis**：并列关系
- **pcomp**：介词补语
- **pobj**：介词宾语
- **poss**：所有格修饰语
- **preconj**：前置并列连词
- **predet**：前限定词
- **prep**：介词
- **prt**：小品词
- **punct**：标点符号
- **quantmod**：数量修饰语
- **relcl**：关系从句
- **root**：根节点
- **xcomp**：开放性补足语

## 参考资料

- [spaCy 词性标签说明](https://spacy.io/api/annotation#pos-tagging)
- [spaCy 依存关系标签说明](https://spacy.io/api/annotation#dependency-parsing)


## 示例

以下是一些使用 spaCy 词性标签和依存关系标签的示例代码：

```python
import spacy

# 加载英语模型
nlp = spacy.load('en_core_web_sm')

# 示例句子
sentence = "The quick brown fox jumps over the lazy dog."

# 处理句子
doc = nlp(sentence)

# 打印每个标记的文本、词性标签、依存关系标签和中心词
for token in doc:
    print(f"标记：{token.text}\t词性：{token.pos_}\t依存关系：{token.dep_}\t中心词：{token.head.text}")

标记：The      词性：DET    依存关系：det     中心词：fox
标记：quick    词性：ADJ    依存关系：amod    中心词：fox
标记：brown    词性：ADJ    依存关系：amod    中心词：fox
标记：fox      词性：NOUN   依存关系：nsubj   中心词：jumps
标记：jumps    词性：VERB   依存关系：ROOT    中心词：jumps
标记：over     词性：ADP    依存关系：prep    中心词：jumps
标记：the      词性：DET    依存关系：det     中心词：dog
标记：lazy     词性：ADJ    依存关系：amod    中心词：dog
标记：dog      词性：NOUN   依存关系：pobj    中心词：over
标记：.        词性：PUNCT  依存关系：punct   中心词：jumps
```

## 其他实用工具
### 1. 命名实体识别（Named Entity Recognition）

```python
import spacy

# 加载英语模型
nlp = spacy.load('en_core_web_sm')

# 示例句子
doc = nlp("Apple is looking at buying U.K. startup for $1 billion.")

# 打印识别到的命名实体及其类型
for ent in doc.ents:
    print(f"实体：{ent.text}\t类型：{ent.label_}")

```
输出：
```
实体：Apple	类型：ORG
实体：U.K.	类型：GPE
实体：$1 billion	类型：MONEY
```

### 2. 词形还原（Lemmatization）
```python
import spacy

# 加载英语模型
nlp = spacy.load('en_core_web_sm')

# 示例句子
doc = nlp("The children were playing in the garden.")

# 打印每个单词的文本和词形还原形式
for token in doc:
    print(f"单词：{token.text}\t词形还原：{token.lemma_}")

```
输出：
```
单词：The	词形还原：the
单词：children	词形还原：child
单词：were	词形还原：be
单词：playing	词形还原：play
单词：in	词形还原：in
单词：the	词形还原：the
单词：garden	词形还原：garden
单词：.	词形还原：.
```

