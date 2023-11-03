import subprocess

# print('generating data')
# subprocess.run(['python', 'generate_axiedashboard_data.py'], cwd='C:\\Users\\bobgu\\Desktop\\record all sales july 2023\\walletpy\\marketfloor\\')


print('copying data to local app folder')
subprocess.run(['python', 'copy_local_data.py'])


print('generating HTML for website')
subprocess.run(['python', 'generate_html.py'])



print('pushing data updates to github. website should be live in 40 seconds')
git_add = 'git add .'
git_commit = 'git commit -m "data update"'
git_push = 'git push origin main'
subprocess.run(git_add, shell=True)
subprocess.run(git_commit, shell=True)
subprocess.run(git_push, shell=True)