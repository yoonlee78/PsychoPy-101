ANACONDA에서 PsychoPy 작업을 위해 필요한 것들. 

1) 아나콘다 설치 (ver. 3.6)
2) 아나콘다 내 작업 환경(environment) 구축
3) 필요 패키지 설치
4) import + window만들어서 확인해보기 (<- 다음 장에서)


1) [Anaconda](Anaconda.com) 설치

2) 아나콘다 내 작업 환경 구축

두 가지 방법이 있습니다. 하나는 <br>
  1) 아나콘다 네비게이터 > 왼쪽 코너 탭에서 **"Environments"** ("Home" 밑에 위치) > "Create" > Name에는 환경 이름 지정해주세요. <br>
  저는 우선 "PsychoPy"라고 지을게요. Packages 선택에는 Python 2.7로 해주세요. (3.6버전이 출시되긴했으나 안정성을 위해 당분간은 2.7로 유지하는걸로..)
  
  2) Command 로 접속합니다. (환경이 생성된 후 재생버튼같은걸 누르시면 "Open Terminal"이 있을거에요).
  conda 명령어는 [conda cheatsheet](https://conda.io/docs/_downloads/conda-cheatsheet.pdf)을 참조. 요긴하게 쓸 일이 많아요.
 
 아래 순서대로 해주세요. <br>
 
 1) 환경을 만듭니다. 아래 예제 코드에서 환경 이름은 "psychopy"입니다. <br>
 
 즉, 콘다에 이렇게 명령할 겁니다.<br>
 
 _만들어라, -안에, "환경이름(psychopy)"라는 이름의 환경을, 언어는 파이썬 2.7로._ <br>
 
 conda create -n psychopy python=2.7 <br>
 
 2) 환경 목록을 불러옵니다.  <br>
  
  conda info --envs
  
 3) 방금 만든 환경을 활성화 할거에요. 즉 이 환경에서 작업하기 위해 그 환경으로 들어간다고 생각하시면 되요. <br>
 
 conda activate 환경이름 (방금 만든 환경 이름을 넣어주세요, 여기선 psychopy겠죠?)<br>
  
 3) 환경 목록에 어떤 패키지가 있는지 확인할 수 있습니다. 여기에 패키지를 새로 설치할 때마다 하나 둘씩 늘어날 거에요. <br>
 확인을 했다면 이제 필요한 패키지를 설치합시다. <br>
 먼저 wxpython을 설치하세요.<br>
 
 conda install wxpython <br>
 
 그러고나면 dependecy와 같이 설치될 패키지의 목록이 나옵니다. 아마 wxpython, future, backports.lzma..등이 나오고 총 패키지의
 크기가 나올거에요. Proceed ([y]/n)? 옆에 커서가 깜빡거리면 "y"를 입력하세요. Download가 진행됩니다. <br>
 
 마찬가지로 다음 패키지들을 설치해주세요.<br>
 pip install pyglet pygame psychopy <br>
 
 다운로드 실행 중 Mac일 경우 개발자용 소프트웨어 설치 권장이 나오면서 설치 오류가 생길 수도 있어요. <br>
 ("에러명:  xcode-select: note: no developer tools were found at '/Applications/Xcode.app', requesting install. Choose an option in the dialog to download the command line developer tools.
  error: command 'gcc' failed with exit status 1.."라고 나올 겁니다). 
  맥에서 자동으로 소프트웨어 설치 권장 메세지가 나올테니 설치해주시면 됩니다. <br> 
  설치가 완료되면 아래 코드로 재도전!<br>
  
  pip install psychopy <br>
  
  아마 성공적으로 다운로드가 되면 아래와 같은 메시지가 나올 겁니다. <br>
  "Successfully built greenlet..."으로 시작되는 메세지인데, 여러 패키지가 따라오는데 그 중에 Psychopy가 있을거에요!<br>

이제 코드 연습에 필요한 플랫폼 하나를 더 설치합시다. Juypter notebook 이란 툴이에요. 설치는 간단해요 위 패키지 설치한대로 똑같이 하시면 되요. <br

conda install jupyter notebook

설치 확인은 바로 activate을 해보거나 safe하게 conda info --envs로 체크!

----- 환경 구성은 여기까지 입니다. 이제 주피터 노트북으로 들어가서 방금 설치한 psychopy 라이브러리와 그 외 필요한 라이브러리를 불러올 거에요(import)
다음 장에서 계속! ---- 

