clear
echo "*****************************************************************"
echo "*                                                               *"
echo "*                    CiteSpace                                  *"
echo "*                                                               *" 
echo "*   RAM:                                                        *"
echo "*     -Xms1g: request at least 1GB ram for Java Virtual Machine *"
echo "*     -Xmx1g: request at most 1GB, depending on your computer   *"
echo "*     -Xss5m: request 5MB ram for Java stack                    *"
echo "*   Locale:                                                     *"
echo "*     US: US/en	    UK: GB/en        Portuguese: BR/pt          *"
echo "*     Chinese: CN/zh    German: DE/de    Korean: KR/ko          *"
echo "*                                                               *"
echo "*****************************************************************"

echo "\n"
echo "Enter the number of your locale from the following options:"

options=("USA: US, en" "Chinese: CN, zh" "Any Other Locale, i.e. country/language" "Exit")
select opt in "${options[@]}"
do
    case $opt in
        "USA: US, en" )
            java -Dfile.encoding=UTF-8 -Duser.country=US -Duser.language=en -Xms1g -Xmx4g -Xss5m -jar CiteSpaceV.jar 
            break            
            ;;
        "Chinese: CN, zh")
            java -Dfile.encoding=UTF-8 -Duser.country=CN -Duser.language=zh -Xms1g -Xmx4g -Xss5m -jar CiteSpaceV.jar 
            break
            ;;
        "Any Other Locale, i.e. country/language")
            java -Dfile.encoding=UTF-8 -Duser.country=US -Duser.language=en -Xms1g -Xmx4g -Xss5m -jar CiteSpaceV.jar 
            break
            ;;
        "Exit")
            break
            ;;
        *) break ;;
    esac
done