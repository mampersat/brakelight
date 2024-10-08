# Brake Light
Replacement brake light for motorcycle with blinky and secret powers

![Installed](images/brakelight.gif)

## Prototype with test button
<img src="images/prototype.png" alt="prototype" width=512/>

## Inspiration
[Amazon version for $29.95](https://www.amazon.com/dp/B002TS2G9Y/ref=vp_m_vp_dp_m_dex_ai_hr_loc_mtl_pd?_encoding=UTF8&pf_rd_p=f7581ae5-3997-4dd6-a4f6-7dbe08aa8791&pf_rd_r=ZY0FS6N7PC5APMGQ3JSH&pd_rd_wg=mI0bg&pd_rd_i=B002TS2G9Y&pd_rd_w=GMkL9&content-id=amzn1.sym.f7581ae5-3997-4dd6-a4f6-7dbe08aa8791&pd_rd_r=c63c6def-2e24-41c0-bdc3-9324f95dface&psc=1) : No secret powers

## Hardware
* [Original Brakelight](https://www.ebay.com/itm/235594788595?chn=ps&norover=1&mkevt=1&mkrid=711-166974-028196-7&mkcid=2&mkscid=101&itemid=235594788595&targetid=2274951440814&device=c&mktype=pla&googleloc=9002355&poi=&campaignid=21623111277&mkgroupid=172133702611&rlsatarget=pla-2274951440814&abcId=10001153&merchantid=7921664&geoid=9002355&gad_source=1&gclid=CjwKCAjwl6-3BhBWEiwApN6_kig4rh1KD76QaW8gjmniJRpjkIyIZi-10f_q1j0Sk4a1UfQUgmsTsRoCYY0QAvD_BwE) : In case this goes horribly wrong
* [Raspberry PI Pivo W](https://www.amazon.com/KEYESTUDIO-Raspberry-Starter-Headers-Breadboard/dp/B0861WJ2DD/ref=sr_1_2_sspa?crid=1XWHMXDIABI73&dib=eyJ2IjoiMSJ9.TJIpZP0bTFZxMU6MOg346F0AwDi6wPxPEpdv-gz9axYy-r9zx5F11QmrxPkcc7EJ9-z2FLFnnt2tIAN7EOFtNts8T-YRWzKnfL1uR8azv_aYbyauJ8kQQAvI_pcOZlGpbPzCJ4559DUcCKyPHtb-zpY9l6X1qmJgHYvHGav62GRtu3EfHJU6odAHozK2X2AHGcKQxZz_m5gx-hSlQYxaBM9i3A5LxwBcDcCm5jREzSs.Jw9crYVdsixrxqcTKcf2CEw_9eaFbfQcOFZC746vuKM&dib_tag=se&keywords=pi+pico+W&qid=1727963530&sprefix=pi+pico+w%2Caps%2C98&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1) : Probably doesn't need to be a W, but WHY not
* [NeoPixels](https://www.amazon.com/ALITOVE-Individual-Addressable-Programmable-Non-Waterproof/dp/B01MG49QKD/ref=sr_1_1_sspa?crid=201A5PTBTOOBP&dib=eyJ2IjoiMSJ9.YkMkwC8IioO9gXqYDlLoxkE5zALl9YSkc5NA7IpyJjlIWHPYKgZ9blsX4JyLW-qkFiFHAVub79YRNKGVr7ecS-WRYq92C_H52W2Xy1ZKQ2gl7RN-TT3_xj41_eJhH9PcE4g0PAOsJzHzg6rJecZABXaCgbkIROIFF0UVUATNJkbBAnPQ2x1hgK3jkvrN-1rmmCtrb5wRuqiq-vDPms6nTOefqTibIbyw3aOEY6bd9AsJsH5qBWYi0jtK247jb6SU2EKEVe6DSXx0BCqwaNjFwn6XJldICwC1wNaRh-JqTHM.JirLok02PhFE33RvNeiVyu3r4kn-7m0tj8i5Pgr0Mio&dib_tag=se&keywords=neopixels&qid=1727963578&sprefix=neopixels%2Caps%2C102&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)
* [L7805CV Power stepdown components](https://www.amazon.com/gp/product/B0BRV3HTXY/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&th=1)

## Features
* Functions as normal brakelight until configured otherwise
* Ambulance Mode: Blink the braking mode
* Night Ride Mode: Night rider animation during normal mode + ambulance blink
* Tap Response Modes: Respond to sequences of taps
    * Enabling tap sequence can't interefer with normal operation
    * Turn Mode
        * 3 taps: Left turn for 30s
        * 4 taps: Right turn for 30s
    * Demo Mode
        * 2 taps: Party mode for 1s
        * 3 taps: Party Mode for 1m
        * 4 taps: Explosion
        * 5 taps: Police/Ambulance flashing for 1m
    * Media Control Mode
        * 2 taps + length of next tap: Volume
    * Evil Mode
        * Use wifi to rickroll everyone in range
        * Enabled with morse code for EVIL `. ...- .. .-..`

## Wiring
![Circuit Diagram](images/circut.png)

## Kickstarter
[Started work on this](https://www.kickstarter.com/projects/1743331958/267604435/edit/rewards?tab=items)
* Founders award = Send us your brake light, we'll sned it back rewired
* Supporter 1 = Complete kit: Standard light socket plugs + a strip of neopixels you can just jam into whatever you currently have
* Supporter level 2 = Parts kit: hardware not connected
* Supporter level 3 = I just wanna see it happen

## Brakelights song
<pre>
C (A bouncey C)   G (maybe F?)
Your brakelights  aren't that Bright
C                 G
Espiecially       at night
C                 C
Make'm Blink      Make'm flah
G                 G
Like that car     From Night Rider
</pre>

## License
I dunno... I figure if you use the code and stuff to make money you should gimme a cut. Let's go with MIT for now

MIT License, see [LICENSE](https://github.com/Beta-Technologies/grafana-panel-qrcode/blob/main/LICENSE).

