# create

band = {
    "vocals": 'rahul',
    "guitar": 'rahul'
}

another_band = dict(vocals = 'rahul', guitar = 'rahul')

print(band)
print(another_band)
print(len(another_band))


# access
print(band['vocals'])
print(another_band.get('guitar'))

print(band.keys())
print(band.values())
print(band.items())

# checks
print(('sravya' in band) or ('sravya' in another_band))


# update
band['vocals'] = 'rayoa'
band.update({
    'lyricist': 'sravya'
})
print(band)

# pop
band.update({
    'cordinator': 'rish',
    'assistant': 'sun'
})

print(band.pop('cordinator'))
print(band.popitem())




# delete
band.update({
    'drums': 'a drummer'
})
print(band)
del band['drums']
print(band)

another_band.clear()
print(another_band)

del another_band


# make copies
backup_band = band.copy()

us_band = dict(band)


# nested dics example
nihi = {
    "name": {
        "first": 'nihi',
        "last": 'anapalli',
        "full": 'nihi anapalli',
        "home": 'nini'
    }
}

print(nihi['name']['home'])