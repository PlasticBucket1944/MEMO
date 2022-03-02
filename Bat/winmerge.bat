@ECHO OFF
@REM WinMerge bat実行テスト用バッチ
@REM 参考 https://qiita.com/mima_ita/items/ac21c0588080e73fc458

@REM 実行方法
@REM WinMeregeのパス 比較する物Aのパス 比較する物bのパス
@REM オプション
@REM -or:比較結果を指定のパスに出力 -noninteractive:出力後WinMeregeを終了
@REM -cfg ReportFiles/ReportType=1:tab区切り形式で比較結果を出力 
@REM -r:サブフォルダ含めて比較

WinMerge\WinMergeU HOGE FUGA -or %~dp0\out.txt -noninteractive -cfg ReportFiles/ReportType=1 -r
