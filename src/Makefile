LANG=da_DK.ISO8859-1

sprog=dansk
sprog_en=Danish
sprog_en_lower_case=danish
language_code=da
country_code=DK

lang=da
version=1.7.42

installdir_old=`locate wordbook/dictionary.lst | sed 's:/dictionary.lst$$::'`
installdir_new=`locate /share/dict/ooo | perl -pe 'use locale; s:^(.*/share/dict/ooo).*$$:$$1:' | sort -u | tail -1`

installdir_user=$(HOME)/.openoffice/user/wordbook

all:

install: $(language_code)_$(country_code).dic $(language_code)_$(country_code).aff
	if [ -d "$(installdir_old)" ]; then install -o root -g root -m 0644 $(language_code)_$(country_code).dic $(installdir_old); echo old location; fi
	if [ -d "$(installdir_old)" ]; then install -o root -g root -m 0644 $(language_code)_$(country_code).aff $(installdir_old); echo old location; fi
	if [ -d "$(installdir_new)" ]; then install -o root -g root -m 0644 $(language_code)_$(country_code).dic $(installdir_new); echo new location; fi
	if [ -d "$(installdir_new)" ]; then install -o root -g root -m 0644 $(language_code)_$(country_code).aff $(installdir_new); echo new location; fi

user_install: $(language_code)_$(country_code).dic $(language_code)_$(country_code).aff
	@mkdir -p $(installdir_user)
	@if [ -d "$(installdir_user)" ]; then cp -p $(language_code)_$(country_code).dic $(language_code)_$(country_code).aff $(installdir_user)/; echo DICT el GR $(language_code)_$(country_code) >> $(installdir_user)/dictionary.lst; echo DICT $(language_code) $(country_code) $(language_code)_$(country_code) >> $(installdir_user)/dictionary.lst; echo user location; else echo can not install; exit -1; fi

clean:

