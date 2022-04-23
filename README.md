# CalculateLibrary

## runtime.txt
负责部署到heroku的python版本，注意格式python-3.10.2
可以使用`python --version`查看自己使用的python版本

## workflow
注意设置抓取所有内容
```yml
- uses: actions/checkout@v3
      with:
        # Fetch all history for all tags and branches
        fetch-depth: 0
```
注意设置环境
```yml
environment: HEROKU_API_TOKEN
```
部署
```
- name: Deploy to Heroku
      env:
        HEROKU_API_TOKEN: ${{ secrets.HEROKU_API_TOKEN }}
        HEROKU_APP_NAME: ${{ secrets.HEROKU_APP_NAME }}
      if: github.ref == 'refs/heads/master' && job.status == 'success'
      run: |
        git remote add heroku https://heroku:$HEROKU_API_TOKEN@git.heroku.com/$HEROKU_APP_NAME.git
        git push heroku HEAD:master -f
```