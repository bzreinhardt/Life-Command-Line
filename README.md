# Life Command Line
This is just a set of command line tools for common things I do on the computer

To set up aliasing, add this line to bash profile:
`export LIFE_COMMAND_LINE_FOLDER=<full path to this folder>`

I alias them so they're even faster: current `~/.bash_profile` contains:  
`
alias combine-pdfs='bash $LIFE_COMMAND_LINE_FOLDER/combine-pdfs.bash'
alias who='python $LIFE_COMMAND_LINE_FOLDER/find_linkedin_address.py'
alias intro='python $LIFE_COMMAND_LINE_FOLDER/compose_intro_email.py'
alias mountain='python $LIFE_COMMAND_LINE_FOLDER/find_mountain_project.py'
alias upload='python $LIFE_COMMAND_LINE_FOLDER/upload_picture_to_s3.py'
alias compress='bash $LIFE_COMMAND_LINE_FOLDER/compress_podcast.bash'
alias finance='bas $LIFE_COMMAND_LINE_FOLDER/finance.bash'
`
