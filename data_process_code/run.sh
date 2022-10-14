for i in data0 data1
do 
    
    python data_process.py --data_path $i \
        --save_path $i/train --val_path $i/val

done