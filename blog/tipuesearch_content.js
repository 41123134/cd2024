var tipuesearch = {"pages":[{"title":"About","text":"cmsimde 內容管理系統 倉儲: https://github.com/41123134/cd2024/ 網站: https://41123134.github.io/cd2024/ 簡報: https://41123134.github.io/cd2024/reveal 網誌: https://41123134.github.io/cd2024/blog","tags":"misc","url":"./pages/about/"},{"title":"W11","text":"2024/05/03 上課內容 W11分組任務","tags":"W11","url":"./W11.html"},{"title":"W10","text":"2024/04/26 上課內容 W10分組任務 W10任務一: 列出 2a 各學員評分相關網站 以下為各學員的倉儲的程式 from browser import window, ajax, document, html def fetch_csv_data(): # CSV 檔案網址 url = \"https://mdecd2024.github.io/2astud-2asite/downloads/2a.txt\" def on_complete(req): if req.status == 200 or req.status == 0: # 讀取 CSV 檔案內容 content = req.text # 依照換行符號拆分資料 lines = content.split('\\n') # 建立空列表儲存資料 data = [] # 遍歷每一行資料 for line in lines: # 忽略空白行 if line.strip() == \"\": continue # 依照逗號拆分資料 items = line.split(',') # 將拆分後的資料加入列表 data.append(items) # 必須去除 data 的第一列標題資料, 只取序號為 1 之後的資料 data = data[1:] # 取得 html 可以插入的標註位置 brython_div = document[\"brython_div1\"] course_title = \"cd2024\" # 逐一處理學員資料 index = 0 for items in data: index += 1 student_id, github_username, group = items if github_username == \"\": github_username = \"000\" # 建立網站和倉儲連結，使用正確的模板 site_url = f\"https://{github_username}.github.io/{course_title}\" repo_url = f\"https://github.com/{github_username}/{course_title}\" group_site_url = f\"https://mdecd2024.github.io/2a-midag{group}\" group_repo_url = f\"https://github.com/mdecd2024/2a-midag{group}\" # 添加學號, 網站, 倉儲連結和序號到 brython_div brython_div <= str(index) + \". \" + html.A(student_id, href=site_url) brython_div <= \" (\" brython_div <= html.A(\"repo\", href=repo_url) brython_div <= \") | \" brython_div <= html.A(\"Group Site\", href=group_site_url) brython_div <= \" | \" brython_div <= html.A(\"Group Repo\", href=group_repo_url) brython_div <= html.BR() else: print(\"Error:\", req.text) # 發送 AJAX 請求 req = ajax.ajax() req.bind('complete', on_complete) req.open('GET', url, True) req.set_header('content-type', 'application/x-www-form-urlencoded') req.send() # 呼叫函式讀取 CSV 資料 fetch_csv_data() W10任務二:下載 cd2024_ball_balancing_platform_control_ref.7z此檔案，觀看內容並整理出大綱。 W10任務三:小組分配繪圖，鋼球平衡台零組件繪圖。 已完成","tags":"W10","url":"./W10.html"},{"title":"W9","text":"2024/04/19 上課內容 W9分組任務 在teams中進入Excel表格，填寫期中成積自評表。 上傳期中影片至個人網頁。 期中影片連結 期中影片 [個人網站] [個人網站]：https://d30405d9-41b5-423f-9dab-c679e2364990-00-1zij1i5777u6y.janeway.replit.dev/get_page/%E6%9C%9F%E4%B8%AD%E5%BD%B1%E7%89%87","tags":"W9","url":"./W9.html"},{"title":"W8","text":"2024/04/12 上課內容 W8分組任務","tags":"W8","url":"./W8.html"},{"title":"W7","text":"2024/04/05 上課內容 W7分組任務 本週清明放假，無上課。","tags":"W7","url":"./W7.html"},{"title":"W6","text":"2024/03/29 上課內容 W6分組任務 將個人倉儲進度推到分組倉儲，將倉儲中的子模組更新至最新進度。","tags":"W6","url":"./W6.html"},{"title":"W5","text":"2024/03/22 上課內容 W5分組任務 將每個上完字幕的教學影片上傳至分組blog，並打上自評分數。 第三組 小組blog","tags":"W5","url":"./W5.html"},{"title":"W4","text":"2024/03/15 上課內容 W4分組任務 將\"cd2024_2a_w2_4_利用 Replit 管理 Github Classroom 分組倉儲\"上字幕,逐字稿和大綱 檔案","tags":"W4","url":"./W4.html"},{"title":"W3","text":"2024/03/08 上課內容 加入分組倉儲子模組 將個人倉儲加入第三組倉儲，子模組代號:41123134 @ 229f63c 第三組 倉儲連結","tags":"W3","url":"./W3.html"},{"title":"W2","text":"2024/03/01 上課內容 加入第三組 第三組 倉儲連結","tags":"W2","url":"./W2.html"},{"title":"W1","text":"2024/02/23 上課內容 加入課程teams 課程代碼p0961sy 建立倉儲cd2024 41123134的 倉儲連結 建立cd2024網站 41123134的 網站連結 學習使用網誌 41123134的 網誌連結","tags":"W1","url":"./W1.html"},{"title":"2024 Spring 課程","text":"2024 Spring 網際內容管理與協同產品設計實習課程教學導引. 內容管理系統 使用者可以自行利用 cmsimde_site 倉儲作為 Template, 建立自己的網站內容管理系統. 引用網站網址連結的方法: cmsimde_site - 在文章中多次引用同一個網站連結時, 可以使用此種方法. https://github.com/mdecycu/cmsimde_site - 假如想要快速將網址套用 html 網站連結, 可以使用此種方法. cmsimde_site - 也可以使用 Markdown 的標準網站連結使用格式. # 引用 Python 程式的方法 for i in range(10): print(i, \"列出字串\") 也可以直接在 .md 檔案中使用 html 標註, 或加入 Javascript 或 Brython 程式碼. 從 1 累加到 100: 1 add to 100 將 iterable 與 iterator 相關說明 , 利用 Brython 與 Ace Editor 整理在這個頁面. Filename: .py Run Output 清除輸出區 清除繪圖區 Reload 從 1 累加到 100 part2: 1 add to 100 cango_three_gears BSnake AI Tetris Rotating Block Filename: .py Run Output 清除輸出區 清除繪圖區 Reload","tags":"w1","url":"./2024-Spring-w1-blog-tutorial.html"}]};