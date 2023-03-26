if [ $# != 2 ]; then
    echo 引数エラー: $*
    exit 1
else
    echo $1/$2
    rm outputs/$1/$2
    rm origins/$1/$2
fi