# pip install allure-pytest
#
# just execute test 'pytest -v -s allure_1.py'
#
# to generate allure report you need to use
# pytest -v -s --alluredir="../../Allure_report" allure_1.py
# it's execute test and generating files for report
#
# to show report open CMD and
# allure serve %PATH TO THE FOLDER WHERE REPORT%
# example
# allure serve ../../Allure_report
#
#
# report in temp location and you can't simple share it
# to SHARE you need to use https://www.netlify.com/
# and just drag and drop. You got link and can just open report