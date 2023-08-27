#! /bin/bash
case "${1}" in
    #目标文件行数
    target_num)
    target_num_value=`cat /root/batch_fofa_api/target.txt | wc -l`
    echo "${target_num_value}"
    ;;

    #目标文件去重
    uniqfofa_batch)
    sort /root/batch_fofa_api/target.txt | uniq >  /root/batch_fofa_api/target_tmp.txt
    cp /root/batch_fofa_api/target_tmp.txt /root/batch_fofa_api/target.txt
    ;;
esac
