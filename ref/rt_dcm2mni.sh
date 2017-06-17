#!/bin/sh

set -u

subjectName=$1
scanNum=$2
longScanNum=$(seq -f "%02g" $scanNum $scanNum)


imgDir='/mnt/Data01/'`date +%Y%m%d`'.'$subjectName'.'$subjectName''
#imgDir='/mnt/Data01/20161018.1018162_phantom01.1018162_phantom02'
delta=0.0001  #seconds

stamp=`date +%Y%m%d%H%M%S`
echo $imgDir

regFile=${imgDir}/reg/f2mni.feat/reg/example_func2standard.mat
templateFile=/mnt/Data01/offline/strongbad01/anat4mm/canonical.nii.gz


for fileNum in $(seq -f "%04g" 1 9999)
do

    fileName=$imgDir/'001_0000'$longScanNum'_00'$fileNum.dcm
    echo awaiting $scanNum $fileNum
    while [ ! -f $fileName ]
    do
	#echo 1
        sleep $delta
    done

    echo `date +%s.%N ` >> ./timing_logs/file_arrival_$stamp.txt

    go=$(date +%s.%N)
    echo changing mod/waiting for filewrite
    sleep .02
    sudo chmod +r $fileName
    sleep .02
    bc <<<  "$(date +%s.%N)-$go"

    # convert to nii
    echo dcm2niix $scanNum $fileNum
    dcm2niix -s -f %n_%s $fileName > /dev/null
    mv ${imgDir}/${subjectName}_${scanNum}.nii ${imgDir}/${longScanNum}_${fileNum}.nii
#    mv ${imgDir}/${subjectName}_18.nii ${imgDir}/${longScanNum}_${fileNum}.nii
    bc <<<  "$(date +%s.%N)-$go"

    # convert to mni
    echo sub2mni $scanNum $fileNum
    fsl5.0-flirt -in ${imgDir}/${longScanNum}_${fileNum}.nii -ref $templateFile -applyxfm -init $regFile -out ${imgDir}/ppnii/w${longScanNum}_${fileNum}.nii
    bc <<<  "$(date +%s.%N)-$go"

    echo `date +%s.%N ` >> ./timing_logs/post_nii_mni_$stamp.txt

done

# python ./classifier/nifti_file_watcher.py tmp ../brainiak_cloud/sb_714.npy ../brainiak_cloud/allsubs_select_seq_top2000.nii.gz ../brainiak_cloud/svm_all_2000.pkl -w 20 -t 714 &
# ./bin/copy_files.sh ../brainiak_cloud/20161219.1219161_rtstrongbad01.1219161_rtstrongbad01/ppnii/*.nii.gz tmp 0.5

# dcm2niix -s -f ../brainiak_cloud/001_000011_000139.dcm  > /dev/null
# fsl5.0-flirt -in brainiak_cloud_TR1000ms_Slice44_Res2.5iso_100phase_noG_20161219102259_11.nii -ref canonical.nii.gz -applyxfm -init example_func2standard.mat -out ppnii.nii

# curl -X POST -H "Cache-Control: no-cache" -H "Postman-Token: a01cb4c1-b9f9-cde3-6ceb-c7cab07740e2" -H "Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -F "file=@/Users/dsuo/Downloads/001_000011_000139.dcm" "http://ec2-52-207-158-247.compute-1.amazonaws.com:5000/rtfcma-prisma/"
