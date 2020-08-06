#rm -r output
mkdir output
pip3 install -r requirements.txt --no-deps -t output
cp -r src/* output/
cd output
zip -r ../output.zip *