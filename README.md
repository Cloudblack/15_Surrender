<div align="center">
  
# 적극 15분 항복 권장 서비스
  
</div>
### 프로젝트 기간
2021/10/06 ~ 2021/10/13

### 목차
- [프로젝트 배경](#프로젝트-배경)  
- [프로젝트 진행](#프로젝트-진행)
- [데이터 수집](#데이터-수집)
- [데이터 분석](#데이터-분석)
- [모델](#모델)
- [베타 테스트](#베타-테스트)
- [서비스 개발](#서비스-개발)
- [실전 테스트](#실전-테스트)
- [한계 및 문제점](#한계-및-문제점)



## 프로젝트 배경
<img src="https://user-images.githubusercontent.com/86823305/171424092-6d989dae-c477-4198-a977-b3650ec77f21.png"  width="800" />

롤이라는 게임은 

한 팀에는 5명의 플레이어가 있고 
여러 방법으로 적 본진으로 향하여 넥서스를 부시는게 목표입니다 
물론 상대편에도 5명의 플레이어가 있으며 보통 한판에 30~40분이 걸립니다
<br>

오래전, 시즌 막바지 친구가 실버 승급전을 대신 해주면 치킨을 사준다고 제안 했고 
5판 중 3번을 이기면 되는데 여유롭게 2승 0패, 한판만 이기면 되는 상황이라  치킨을 미리 시켰습니다 

그런데 이상해지는 게임 급기야 서로 싸우기 시작했고 팀에선 15분에 빠른 항복 투표를 합니다 팀은 지고있긴 했지만 저는 엄청나게 성장해서 질 것 같지않았습니다

당연히 저는 항복을 거부했습니다 결과는 

<img src="https://user-images.githubusercontent.com/86823305/171424940-7f0a59ff-f6ab-4ecb-9b79-8cf0ba2b3658.png"  width="300" />


당연하게도 패배, 
줄타기 하듯 1시간 40분에 걸친 게임을 지며 몸은 지치고 멘탈은 박살났습니다.
2승 1패,  시즌 종료까지 남은시간은 45분, 사실상 마지막 한판이 되어 여유는 사라지고 뒤에서 식어가고있는 치킨처럼 제 손도 식어갔습니다 

우려와 다르게 14분만에 게임을 이기고 치킨을 먹었습니다
하지만.. 이미 부서진 멘탈은 치킨으로도 치유되지않았습니다. 

<img src="https://user-images.githubusercontent.com/86823305/171425009-eb50e475-8ab9-4b06-890d-46c46c679943.png"  width="300" />

만약, 15분 항복때 내가 그 판에 결과를 예측 할 수 있었다면 
멘탈 터질 일 없이 행복 롤을 하고  치킨파티를 하고있지 않았을까요? 

그래서 제가 준비한 것은 적극 15분 항복 권장 서비스로 
15분의 데이터를 바탕으로 승률을 예측해 빠른 서렌을 권장, 플레이어의 시간과 멘탈을 보호합니다




# 프로젝트 진행
## 데이터 수집
<img src="https://user-images.githubusercontent.com/86823305/171425700-55ecd863-b0fc-4cc3-a461-a51eac23a397.png"  width="800" />

- API에서 정보를 받아 저장하고 예측모델을 서비스로 만들 계획입니다

<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171426275-7cc7e93f-8c95-4109-8930-87c70e857e54.png"  width="600" />

먼저 riot api를 받습니다 24시간 마다 갱신을 해줘야 합니다 문제는 리퀘스트를 2분에 100회밖에 할 수 없다는 것입니다  
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171426338-cf6408df-61ac-4ead-a564-6e469c06fa1d.png"  width="600" />

먼저 API에서 리그별로 검색해서 플레이어 리스트를 받아옵니다 그러면 플레이어 아이디를 얻을 수가있습니다 
<br>
<br>


<img src="https://user-images.githubusercontent.com/86823305/171426408-81864b52-c0dd-45ee-94dc-4ec7105cad06.png"  width="600" />

플레이어 아이디로 Puuid를 얻습니다   
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171426547-1ee370b8-74e3-4697-bbeb-6cf2f1593963.png"  width="150" />

puuid로 MatchID를 얻습니다   
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171426612-38aa543b-918e-497b-ac5e-452dba8dee1e.png"  width="400" />

MatchId로 드디어 Gamedata를 얻을수있습니다  
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171426662-78f073ea-2ec3-4b2e-bdd4-b39b9a8c09fa.png"  width="600" />

정리하면 플레이어 아이디로 puuid를 얻고 ,puuid로 matchid를 얻고 matchid로 gameid를 얻고 gameid로 게임데이터를 얻습니다  
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171426722-3e11dbf5-154b-45b8-b91c-5df957a53f52.png"  width="800" />

이렇게 2만 8천개의 데이터를 CSV,MongoDB nosql,DB sql 세개의 방식으로 저장했습니다  
<br>
<br>


## 데이터 분석
<img src="https://user-images.githubusercontent.com/86823305/171427301-57fc080f-847d-44b1-8667-024b9204cb83.png"  width="800" />

왼쪽편의 자료가 Api로 얻은 게임데이터인데 Api에서 얻을 수 있는 정보 중 에 실제 게임 중 에는 얻을 수 없는 정보가 존재했고 제거했습니다  
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171427464-d7345a1d-6e08-44f5-8922-adc542e461c7.png"  width="800" />

왼쪽그래프는 블루팀이 이겼을때, 오른쪽은 레드팀이 이겼을때 이며  파란색은 블루팀 빨간색은 레드팀의 지표입니다 , 그래프별로 왼쪽부터 평균 분당cs 평균 kda 평균 레벨 평균 타워파괴 평균 드래곤 획득입니다 당연하지만 승리한팀이 높은 지표를 가지고있습니다  
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171427496-b7af2cb3-81fd-4df4-93d7-02ea0b9d5fd0.png"  width="800" />

각 팀이 승리했을때의 이긴팀과 진팀의 지표의 차입니다 어느정도 차이가 있는건 알겠지만 비교하기 좀 힘듭니다  
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171427560-5de32af6-5fa9-4b64-83dd-b41e47de8da8.png"  width="800" />

이번엔 점유율을 표시했습니다 하프라인일 때는 양팀의 지표가 비슷합니다  이기는 팀은 레벨과 cs는 큰 차이가 없어도 KDA와 타워파괴  드래곤획득이 많은 것을 볼 수있습니다  
<br>
<br>

## 모델 
xgboost를 사용했습니다

<img src="https://user-images.githubusercontent.com/86823305/171427762-70147f90-3467-4072-a965-118faf98298e.png"  width="800" />

그래서 게임 중 사용가능 한 특성들을 기반으로 15분 예측 모델을 만들었고 베이스라인 50%에 비해 약 80%의 예측 확률로 괜찮은 성능을 보입니다  
<br>
<br>

## 베타 테스트
<img src="https://user-images.githubusercontent.com/86823305/171428123-43b92a14-8620-4fc5-9a7f-c2536ea84ad5.png"  width="200" />

베타 테스터에게 15분 데이터를 받아서 예측 모델을 돌려본 결과  
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171428267-0f340439-f5d5-4814-80da-9103948d6976.png"  width="600" />

예측 적중률은 25%... 적은 데이터지만 원인을 분석했고  
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171428493-8adc56c8-5832-4b5f-85f3-10110f201307.png"  width="400" />

문제점으로는 예측하는데 사용한 데이터는 최상위 플레이어의 데이터지만 테스터님은 하위 티어라 제대로된 예측이 안되었습니다  
최상위 티어에서 테스를 할 수 없어 아쉬움이 남는 테스트가 되었습니다  
<br>
<br>

## 서비스 개발
<img src="https://user-images.githubusercontent.com/86823305/171428781-bca0a55d-3430-4e16-b6f9-9a1b52336ef7.png"  width="600" />

개발한 서비스는 왼쪽과 같은 웹 입력창에 각팀의 캐릭터별로 레벨 cs 킬 어시 팀별로 타워와 드래곤 상황 그리고 참고용으로 실제 승리팀까지 총 45개의 데이터를 입력해야합니다   
<br>
<br>

## 실전 테스트



## 한계 및 문제점

<img src="https://user-images.githubusercontent.com/86823305/171429823-8e1d2541-dcab-4db8-a2f4-187ddfedbbca.png"  width="600" />

한계점에 대해 얘기해 보겠습니다 먼저 편의성 문제입니다 게임하다 말고 45개를 입력 할 수 없습니다  
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171429485-24bfde54-f789-4583-a1db-eaa84f798366.png"  width="600" />

데이터 수집의 한계입니다 하나의 게임데이터를 얻기까지 여러 번의 API를 사용해야하는데 일반 회원의 인증키는 한계가 있습니다.  
실제로 프로젝트 기간 중 대부분의 시간을 데이터수집에 사용했고 2.8만개의 게임데이터밖에 얻지못했습니다  
보완방향으로는 개인API키를 프로덕션 API로 바꾸는 방법이 있습니다  
<br>
<br>

<img src="https://user-images.githubusercontent.com/86823305/171429676-ca5288aa-247c-479f-8fcf-2aeae1a35e30.png"  width="600" />

만든 모델의 한계입니다 게임 중 알 수 있는 정보 중에 숫자로 쓸 수 있는 것만 사용하였고   
팀단위로 데이터를 특성을 사용하여 모델의 유연성과 성능이 떨어진다  
<br>
<br>


<img src="https://user-images.githubusercontent.com/86823305/171429724-1ec15b08-76bf-410b-a91b-e3d833fbb9f5.png"  width="600" />

보완 방향으로는 모든 지표를 활용하는 것이다 캐릭터 라인 스펠 룬 아이템까지 승률에 적용한다면 더욱 좋은 모델이 될 수 있을것같다  
<br>
<br>

## 추가 개선 방안
<img src="https://user-images.githubusercontent.com/86823305/171430001-9b447eef-2cea-49b2-90f3-86f37e28d5ad.png"  width="600" />

- 현재 수동으로 업데이트해야하는 API 데이터와 모델생성을 자동으로 변경
- 실시간 게임에 대한 API를 사용해서 모델링 해 볼것
- 서비스를 다른 사용자에게 웹으로 배포 해볼 것
- 서비스를 사용자가 이용한다면 데이터를 기록해 그걸 기반으로 추가서비스 개발
- 서비스의 웹 디자인 및 추가적인 성능을 개선해 볼 것입니다 
