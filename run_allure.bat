rmdir outputs\allure_report\allure_raw/s/q
pytest --alluredir ./outputs/allure_report/allure_raw
copy ".\config\environment.properties" ".\outputs\allure_report\allure_raw\"
allure serve ./outputs/allure_report/allure_raw
