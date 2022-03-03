@ECHO OFF
@REM Sikulix bat実行テスト用バッチ
@REM https://room.sakura.ne.jp/contents/sikulix_para
@REM https://masuo.doorblog.jp/archives/51723880.html

call java -jar %~dp0sikulixide-2.0.4.jar -r %~dp0TEST.py  -- HOGE FUGA
pause
