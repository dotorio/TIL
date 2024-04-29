# README

git restore 파일명 -> 파일 되돌리기(add 하기 전일때)

git restore --staged 파일명 -> 등록되기 전으로 되돌리기(add 한 후)

git rm --cached 파일명 -> 등록되기 전으로 되돌리기(add 한 후)

git commit --amend -> 직전 커밋명 바꾸기

git reset --sort 커밋난수 -> 그 커밋 커밋되기 직전으로 돌아감

git reset --mixed 커밋난수 -> 그 커밋 add되기 전으로 돌아감

git reset --hard 커밋난수 -> 그 커밋 이전 커밋을 싹다 날림 변동사항도 날림
