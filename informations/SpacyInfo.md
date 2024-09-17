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

1. **acl**: 形容词子句修饰（adjectival clause modifier）
2. **acomp**: 形容词补语（adjectival complement）
3. **advcl**: 副词子句修饰（adverbial clause modifier）
4. **advmod**: 副词修饰（adverbial modifier）
5. **agent**: 施动者（agent）
6. **amod**: 形容词修饰（adjectival modifier）
7. **appos**: 同位语（appositional modifier）
8. **attr**: 属性（attribute）
9. **aux**: 助动词（auxiliary）
10. **auxpass**: 被动助动词（passive auxiliary）
11. **case**: 介词或格标记（case marking）
12. **cc**: 并列连词（coordinating conjunction）
13. **ccomp**: 补语从句（clausal complement）
14. **compound**: 复合词（compound）
15. **conj**: 并列（conjunct）
16. **cop**: 系动词（copula）
17. **csubj**: 从句主语（clausal subject）
18. **csubjpass**: 从句被动主语（clausal passive subject）
19. **dative**: 与格补语（dative）
20. **dep**: 未分类依存关系（unspecified dependency）
21. **det**: 限定词（determiner）
22. **dobj**: 直接宾语（direct object）
23. **expl**: 语势词（expletive）
24. **fixed**: 固定表达（fixed expression）
25. **flat**: 扁平结构（flat）
26. **goeswith**: 缺失单词的同伴（goes with）
27. **iobj**: 间接宾语（indirect object）
28. **intj**: 感叹词（interjection）
29. **list**: 列表（list）
30. **mark**: 从句标记（marker）
31. **meta**: 元数据（meta modifier）
32. **neg**: 否定标记（negation modifier）
33. **nmod**: 名词修饰语（nominal modifier）
34. **npadvmod**: 名词短语副词修饰语（noun phrase as adverbial modifier）
35. **nsubj**: 名词主语（nominal subject）
36. **nsubjpass**: 名词被动主语（passive nominal subject）
37. **num**: 数词（numeric modifier）
38. **number**: 数词成分（element of compound number）
39. **nummod**: 数量修饰（numeric modifier）
40. **oprd**: 开放补语（object predicate）
41. **obj**: 宾语（object）
42. **obl**: 非核心成分（oblique nominal）
43. **orphan**: 孤立成分（orphan）
44. **parataxis**: 并列语法（parataxis）
45. **pcomp**: 介词补语（complement of a preposition）
46. **pobj**: 介词宾语（object of a preposition）
47. **poss**: 所有格修饰语（possessive modifier）
48. **preconj**: 前置并列连词（pre-correlative conjunction）
49. **predet**: 前置限定词（pre-determiner）
50. **prep**: 介词修饰（prepositional modifier）
51. **prt**: 小品词（particle）
52. **punct**: 标点（punctuation）
53. **quantmod**: 量词修饰语（modifier of quantifier）
54. **relcl**: 关系从句修饰语（relative clause modifier）
55. **reparandum**: 修正成分（reparandum）
56. **root**: 根节点（root）
57. **vocative**: 呼语（vocative）
58. **xcomp**: 开放补语（open clausal complement）


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

