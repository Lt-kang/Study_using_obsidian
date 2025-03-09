sklearn.metrics - classification_report
pd.melt
sklearn.metrics.confusion_matrix
tensorflow.keras.preprocessing.image.ImageDataGenerator
plt.annotate()
plt.xscale()
z-score
t검정
중심극한정리
p-value
순열검정
비모수검정
scipy.stats.zscore()
scipy.stats.cdf()
scipy.stats.norm.ppf()
scipy.stats.ttest_ind()
scipy.stats.permutation_test()
sklearn - fit_intercept
datetime - strftime
matplotlib - tight_layout
numpy - where
numpy - where vs pandas - query
!pandoc report.ipynb -s -o report.docx => j노트북을 html or pdf로 저장할 수 있다!
df.info(max_cols = np.inf)
sklearn - tree - plot_tree(model)
seaborn - heatmap & numpy - triu_indices_from
scipy - stats - ttest_ind
numpy - argmax
pandas&numpy - var(ddof)ff
Chardet.detect
Replace와 정규식
Df.str.contains
Df.gt / df.lt
numpy - histogram_bin_deges
plt - yscale('log') / xscale('log')
plt.plot(vert=False)
plt.rcParams / rc()i
plt.annotate(, xytext=, textcoords=)
plt.colorbar() / plt.plot(cmap=)
기하 평균
공분산
상관계수
python - positional-Only Arguments vs Keyword-Only Arguments
python - *args, **kargs
plt.grid
plt.axvline / axhline
sympy - limit
np - meshgrid
np - 행렬곱과 dot product의 차이
np - linalg.inv
pandas 객체 간 연산 / 객체 내 연산 https://wikidocs.net/151739
실함수vvcx
벡터함수
르베그 적분 함수
python - cellections.Counter
python - sympy - expand, factor, solve, Livit, S, Symbol, Derivative
numpy - linalg - matrix_rank()
tf.one_hot
cross_validate(df, X, y, cv=StratifiedKFold())
cross_validate(df, X, y, cv=KFold())
PCA와 설명된 분산
keras.utils.plot_model(model, show_shapes=True)
tf.reduce_mean()
tensor.assign_sub()
tf.multiply()
tf.set_random_seed()
tf.matmul()
tf.div()
tf.train.GradientDescentOptimizier()
optimizer.apply_gradients()
tf.equal()
tf.argmax()
tf.one_hot()
annealing the learning rate
tf.keras.utils.to_categorical()
tf.data.Dataset.from_tensor_slices() / shuffle / prefetch / batch / repeat
tf.train.create_golbal_step()
tf.keras.initializers.glorot_uniform // Xavier initialization (2/(check-in + check-out))
tf.keras.initializers.he_uniform // He initialization (4/(check-in + check-out))
internal Covariate Shift
layer => norm => activation function => drop out
tf.train.exponential_decay()
torch.matmul
torch.mul
torch.squeeze
torch.unsqueeze
torch.mul_ << in-place Operation
torch.zeros
torch.manual_seed()
torch.scatter
np.flip
torch.nn.Module.downsample()
np.eye()
np.squeeze()
autogluon
1차 / 1.5차 / 2차 미분 최적화 알고리즘
립시츠 연속
미니배치의 확률적 성질 / 일반화 오류가 줄어들고 과적합이 방지되는 정규화 효과
가우시안 분포 - L2 규제 / 라슬라스 분포 - L1 규제
numpy에서 float16 ~ 128
np.rand normal binomial uniform
numpy.any / all
np.intersect1d / union1d / in1d / setdiff1d / setxor1d
pd.read_csv / to_csv
pd.get_option / set_option
df.size vs len(df)
df.max() vs df.idxmax()
df.values_counts()
df.loc vs df.iloc
df.set_index / reset_index
np.dot / np.matmul / a*b / a@b
np.linalg.svd vs sklearn.utils.extmath.randomized_svd
시소러스 / 통계 기반 / ppmi & svd
df.loc[다중조건, 칼럼]
df.nlargest()
df.interpolate()
df.columns.str.split(expand=True)
df.set_categories()
df / map vs apply vs applymap
pd.combine_first
df.explode()
df.groupby()[].apply(lambda x: x.describe())
pd.date_range()
pd.bdate_range()
df.truncate()
sns displot / relplot / catplot 
sns stripplot / swarmplot
sns despine
torch rand vs randn
torch fill() vs fill_
torch index_select()
torch mm inverse pinverse trace
torch detach()
np.random.normal
df.iterrows()
MLE
MAP
구구조 구문 분석(규칙 / 통계 / 딥러닝)
의존 구문 분석(규칙 / 통계 / 딥러닝)
의미론 / 화용론
형태소 분석
품사 태깅
의미역 분석
데코레이터
torch.item()
git ssh 
나이브 베이즈
from tokenizers import  BertWordPieceTokenizer
from transformers import  GPT2Tokenizer
from transformers import BertTokenizer
from tokenizers import  ByteLevelBPETokenizer
임베딩
토크나이저(토큰화란?)
CBOW
n-gram
wordpiece
np.inner
few-shot / zero-shot
유니그램
torch.bmm (batch matrix multiplication)
torch.nn.Prarameter / requires_grad
nn은 클래스 / nn.functional은 함수
torch.Tensor.item()
결과 텐서를 인자로 제공 (torch.add(x, y, out=result)
torch.svd
torch.mm
torch.chunk vs split
torch.Tensor.grad_fn
크롤링 vs 스크래핑 vs 파싱
