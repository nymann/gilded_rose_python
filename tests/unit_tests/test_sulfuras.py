from gilded_rose.gilded_rose import GildedRose, Item

def test_sulfuras():
    sulfuras = Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)
    gilded_rose = GildedRose(items=[sulfuras])
    for _ in range(30):
        gilded_rose.update_quality()
        assert sulfuras.quality == 80
        assert sulfuras.sell_in == 10
