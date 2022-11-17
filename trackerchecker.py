import asyncio
import aiohttp

closed_trackers = []
open_trackers = []
URLS = [
    {
        "name": "BeyondHD",
        "url": "https://beyond-hd.me/register/",
        "search_term": "You Must Be Invited To",
    },
    {
        "name": "Acervos",
        "url": "https://acervos.cc/register/null",
        "search_term": "Os registros es",
    },
    {
        "name": "RED-BITS",
        "url": "https://red-bits.com/register/null",
        "search_term": "Has sido devuelto",
    },
    {
        "name": "HDtime",
        "url": "https://hdtime.org/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "HDChina",
        "url": "https://hdchina.org/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "HDChina",
        "url": "https://www.beitai.pt/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "HDCity",
        "url": "https://hdcity.city/signup",
        "search_term": "Free registration not engaged.",
    },
    {
        "name": "AsianCinema",
        "url": "https://asiancinema.me/register/null",
        "search_term": "ust have an invitation link to regist",
    },
    {
        "name": "CinemaZ",
        "url": "https://cinemaz.to/auth/register",
        "search_term": "We sometimes open registration or application. ",
    },
    {
        "name": "PrivateHD",
        "url": "https://privatehd.to/auth/register",
        "search_term": "PrivateHD is Invite Only",
    },
    {
        "name": "eShareNet",
        "url": "https://esharenet.eu/register/null",
        "search_term": "pen Registration is Clos",
    },
    {
        "name": "Aither",
        "url": "https://aither.cc/register/null",
        "search_term": "Open Registration is Closed!",
    },
    {
        "name": "The Horror Charnel",
        "url": "https://horrorcharnel.org/signup.php",
        "search_term": "The site has been set to invite only by the staff<",
    },
    {
        "name": "AvistaZ",
        "url": "https://avistaz.to/auth/register",
        "search_term": "AvistaZ is Invite Only",
    },
    {
        "name": "tv vault",
        "url": "https://tv-vault.me/register.php",
        "search_term": "Sorry, the site is currently invite only",
    },
    {
        "name": "JPTV.CLUB",
        "url": "https://jptv.club/register/null",
        "search_term": "Open registration is closed",
    },
    {
        "name": "RetroFlix",
        "url": "https://retroflix.club/signup.php",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "The New Retro",
        "url": "https://new-retro.eu/signup.php",
        "search_term": "Anmeldung ist leider geschlossen",
    },
    {
        "name": "OshenPT",
        "url": "https://www.oshen.win/signup.php?sitelanguage=6",
        "search_term": "The current user account limit has been reached",
    },
    {
        "name": "Secret Cinema",
        "url": "https://secret-cinema.pw/register.php",
        "search_term": "Sorry, the site is currently invite only.",
    },
    {
        "name": "BwTorrents",
        "url": "https://bwtorrents.tv/signup.php",
        "search_term": "The current users account limit has been reached.",
    },
    {
        "name": "TorrentBytes",
        "url": "https://www.torrentbytes.net/signup.php",
        "search_term": "We're sorry but signups are temporarily closed.",
    },
    {
        "name": "hawke-uno",
        "url": "https://www.hawke.uno/register/null",
        "search_term": "en Registration is Closed",
    },
    {
        "name": "HD-Olimpo",
        "url": "https://hd-olimpo.club/register/null",
        "search_term": "Registro libre cerrado",
    },
    {
        "name": "PassThePopcorn",
        "url": "https://passthepopcorn.me/register.php",
        "search_term": "Sorry, the site is currently invite only.",
    },
    {
        "name": "Torrentland",
        "url": "https://torrentland.li/register/null",
        "search_term": "Registro libre cerrado",
    },
    {
        "name": "BrSociety",
        "url": "https://brsociety.club/register/null",
        "search_term": "Os registros ",
    },
    {
        "name": "UHDBits",
        "url": "https://uhdbits.org/register.php",
        "search_term": "the site is curren",
    },
    {
        "name": "Nebulance",
        "url": "https://nebulance.io/register.php",
        "search_term": "Sorry, registration is currently closed.",
    },
    {
        "name": "AnimeBytes",
        "url": "https://animebytes.tv/register/apply",
        "search_term": "Sorry, applications are",
    },
    {
        "name": "Insane Tracker",
        "url": "https://newinsane.info/signup.php",
        "search_term": "A regiszt",
    },
    {
        "name": "R3V WTF!",
        "url": "https://r3vuk.wtf/signup.php",
        "search_term": "Signups are closed presently",
    },
    {
        "name": "DanishBytes",
        "url": "https://danishbytes.club/register/null",
        "search_term": "Du skal have et invitationslink",
    },
    {
        "name": "Anime Torrents",
        "url": "https://animetorrents.me/register.php",
        "search_term": "Registration Closed",
    },
    {
        "name": "TellyTorrent",
        "url": "https://telly.wtf/register/null",
        "search_term": "pen Registration is Closed",
    },
    {
        "name": "ReelFLiX",
        "url": "https://reelflix.xyz/register/null",
        "search_term": "Open Registration is Closed",
    },
    {
        "name": "PuroVicio",
        "url": "https://purovicio.in/register/null",
        "search_term": "Open Reg Closed",
    },
    {
        "name": "SkipTheTrailers",
        "url": "https://skipthetrailers.xyz/register/null",
        "search_term": "Open Registration is Closed",
    },
    {
        "name": "Gazelle Games",
        "url": "https://gazellegames.net/register.php",
        "search_term": "Registration is currently closed.",
    },
    {
        "name": "Red Star Torrent",
        "url": "http://rstorrent.org.pl/signup.php",
        "search_term": "Nieaktywne konta s",
    },
    {
        "name": "Generation-Free",
        "url": "https://generation-free.org/register/null",
        "search_term": "https://generation-free.org/login",
    },
    {
        "name": "Peeratiko",
        "url": "https://peeratiko.org/signup.php",
        "search_term": "ignups are closed pres",
    },
    {
        "name": "TheScenePlace",
        "url": "https://www.thesceneplace.com/index.php?page=account",
        "search_term": "ry, but registrations are closed",
    },
    {
        "name": "HDMonkey",
        "url": "https://hdmonkey.org/account-signup.php",
        "search_term": "orry this site has disabled user registration",
    },
    {
        "name": "TorrentSeeds",
        "url": "https://torrentseeds.org/buyinvite",
        "search_term": "https://torrentseeds.org/buyinvite",
    },
    {
        "name": "Tophos",
        "url": "https://tophos.org/signup.php",
        "search_term": "Signups are closed presently",
    },
    {
        "name": "HD-F",
        "url": "https://hdf.world/register.php",
        "search_term": "ctuellement sur invitation se",
    },
    {
        "name": "HDFans",
        "url": "https://hdfans.org/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "iHDBits",
        "url": "https://ihdbits.me/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "HHanClub",
        "url": "https://hhanclub.top/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "LemonHD",
        "url": "https://lemonhd.org/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "AlphaRatio",
        "url": "https://alpharatio.cc/register.php",
        "search_term": "e site is currently invite",
    },
    {
        "name": "ExoticaZ",
        "url": "https://exoticaz.to/register",
        "search_term": "metimes open registration or applic",
    },
    {
        "name": "Abnormal",
        "url": "https://abn.lol/Home/Register",
        "search_term": "pour le momen",
    },
    {
        "name": "dream-torrents",
        "url": "http://dream-torrents.com/signup.php",
        "search_term": "gistration is currently disabl",
    },
    {
        "name": "BLUTOPIA",
        "url": "https://blutopia.xyz/register/null",
        "search_term": "Open Registration is Closed",
    },
    {
        "name": "Pornbay",
        "url": "https://pornbay.org/register.php",
        "search_term": "Sorry, registration is currently closed",
    },
    {
        "name": "Orpheus",
        "url": "https://orpheus.network/register.php",
        "search_term": "Sorry, the site is currently invite only.",
    },
    {
        "name": "HD-Torrents",
        "url": "https://hd-torrents.org/account.php",
        "search_term": "You need an invite to join this communit",
    },
    {
        "name": "HDSky",
        "url": "https://hdsky.me/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "TorrentCCF",
        "url": "https://et8.org/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "HDU",
        "url": "https://pt.upxin.net/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "HDU",
        "url": "https://pt.upxin.net/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "TFLBits",
        "url": "https://pt.eastgame.org/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "HDAtmos",
        "url": "https://hdatmos.club/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "HDarea",
        "url": "https://hdarea.co/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "HDZone",
        "url": "https://hdzone.me/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "Ourbits",
        "url": "https://ourbits.club/signup.php?sitelanguage=6",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "SkipTheCommercials",
        "url": "https://skipthecommericals.xyz/register/null",
        "search_term": "Open Registration is Closed",
    },
    {
        "name": "DesiTorrent",
        "url": "https://desitorrents.tv/register/null",
        "search_term": "Open Registration is Closed",
    },
    {
        "name": "HDHome",
        "url": "https://hdhome.org/signup.php",
        "search_term": "817230945",
    },
    {
        "name": "LST",
        "url": "https://lst.gg/register/null",
        "search_term": "pen Registration is",
    },
    {
        "name": "HDRoute",
        "url": "http://hdroute.org/register.php",
        "search_term": "ossibility of re-opening",
    },
    {
        "name": "Bitspyder",
        "url": "https://bitspyder.net/signup.php",
        "search_term": "ou need an invite to Join the Communit",
    },
#    {
#        "name": "Milkie",
#        "url": "https://milkie.cc/auth/signup",
#        "search_term": " At the moment the site is invite only. If you don't have an invite code but still would like to join,",
#    },

]

conn = aiohttp.TCPConnector(limit_per_host=10, limit=10, ttl_dns_cache=300)
PARALLEL_REQUESTS = len(URLS)


async def gather_with_concurrency(n):
    timeout = aiohttp.ClientTimeout(total=30)
    semaphore = asyncio.Semaphore(n)
    session = aiohttp.ClientSession(connector=conn, timeout=timeout)
    print("Starting...")
    async def get(url, name, search_term):
        async with semaphore:
            try:
                async with session.get(url, ssl=False) as response:
                    obj = await response.read()
                    status_code = response.status
                    if status_code > 500:
                        print(f"{name} is down!")
                    elif search_term in str(obj):
                        closed_trackers.append(name)
                    else:
                        print(f"{name} is open! {response.url}")
            except asyncio.exceptions.TimeoutError:
                print(f"{name} timed out!")
                pass
    await asyncio.gather(
        *(
            get(
                url.get("url"),
                url.get("name"),
                url.get("search_term"),
            )
            for url in URLS
        )
    )
    await session.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gather_with_concurrency(PARALLEL_REQUESTS))
    conn.close()

closed_trackers.sort()
closed_trackers = str(closed_trackers).replace("[","")
closed_trackers = closed_trackers.replace("'","")
closed_trackers = closed_trackers.replace("]","")
print(f"\nClosed trackers: {closed_trackers}")
