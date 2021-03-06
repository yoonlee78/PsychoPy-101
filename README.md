# PsychoPy-101
싸이코파이 튜토리얼

디렉토리: 
- Setup : 설치 방법 관련 노트북(.ipynb) 파일
- practice : 실습 예제(스터디)

배경: 

실험심리학에서는 사람의 생각하는 과정을 측정하기 위해 다양한 실험 방법을 씁니다. 지각, 인지, 언어, 사회심리 등 다양한 심리학의 세부분야가 해당됩니다. 많은 검사(또는 과제라고도 합니다)들은 컴퓨터로 설계합니다. 인지심리에서는 주의력, 기억력, 언어 능력 (말하기,읽기,쓰기), 그리고 선택 및 의사결정 등의 주제를 연구하고 실험합니다. 예를 들어, 주의 및 집중 또는 제어력을 검사하는 실험 과제의 대표적인 과제 중, 스트룹 효과를 측정하는 [Stroop Task](http://psychclassics.yorku.ca/Stroop/)가 있습니다. 빨강, 노랑 등의 색깔을 나타내는 단어를 같은 색으로 제시했을 때와 다른 색으로 제시했을 때 단어를 읽는 속도를 비교하고, 다른 색으로 제시했을 때 색깔에 영향받지 않고 단어를 얼마나 빨리 응답하는 지를 측정하는 과제입니다.

이처럼 실험심리 분야에서 쓰이는 다양한 과제를 컴퓨터 언어로 구현하는 것이 중요한데, 대부분은 상용화된 유료 소프트웨어 (e.g., Eprime) 를 많이 써왔지요. 하지만 더 다양하거나 정교한 자극을 사용하고자 할때, 기존의 유료 소프트웨어로 자극 및 과제를 만드는 것에는 한계가 있습니다. 프로그래밍에 조금 익숙한 연구자들은 C 언어나 MATLAB같은 언어로 많이 실험을 설계했습니다. 하지만 이 언어들 역시 초보자가 배우기에는 장벽이 높고, 초보자가 언어를 배워서 실험을 진행할 수 있는 수준까지 구현하기까지는 부담이 많을 수도 있죠. 

영국 노팅엄 대학교의 존 피어스 교수가 이를 개선하고자 2004년에 [PsychoPy](http://www.psychopy.org/)라는 파이썬 라이브러리를 개발했습니다. 그는 시지각을 연구하는 심리학자여서 단순 시각자극(도형, 텍스트)부터 정교한 시각 자극까지 (scale, garbor patch) 사용할 수 있게 해주는 라이브러리입니다. 

심리학의 연구 주제가 다양한 만큼 PsychoPy로 모든 심리학 실험을 구현할 수는 없지만 (예를 들어, VR 연구 같이 3D 시뮬레이션이 필요할 경우, MATLAB이나 Unity같은 게임 개발 도구가 더 맞을 수 있습니다), 파이썬을 처음 접하는 입문자이거나 간단한 자극만을 필요로하는 실험 과제를 만들고자하는 (실험심리) 연구자에게는 적절한 도구라고 생각합니다. 

** 이 레퍼지토리에 올리는 자료들은 연구실(hfpsych.snu.ac.kr)에서 또는 외부 활동/스터디 (feat. [싸이그래머](https://www.facebook.com/groups/psygrammer/))에서 공부한 자료들의 요약입니다. 

**PsychoPy가 온라인 플랫폼 (Pavolvia)으로 전환됨에 따라, 오픈 소스 업데이트가 이전 만큼 활발하지 않습니다. 더 이상 이 깃헙에서는 업데이트되지 않습니다. 

아래는 도움이 될만한 참고 링크입니다: 

[PsychoPy User Forum](https://discourse.psychopy.org/) |
[PsychoPy Tutorial](https://www.youtube.com/watch?v=VV6qhuQgsiI)

Best,

Yoon Kyung Lee, <br>
Ph.D. Candidate in Cognitive Psychology, <br>
SNU <br>
