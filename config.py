examples = [
    "1girl, souryuu asuka langley, neon genesis evangelion, plugsuit, pilot suit, red bodysuit, sitting, crossing legs, black eye patch, cat hat, throne, symmetrical, looking down, from bottom, looking at viewer, outdoors",
    "1boy, male focus, yuuki makoto \(persona 3\), persona 3, black jacket, white shirt, long sleeves, closed mouth, glowing eyes, gun, hair over one eye, holding gun, handgun, looking at viewer, solo, upper body",
    "1girl, makima \(chainsaw man\), chainsaw man, black jacket, black necktie, black pants, braid, business suit, fingernails, formal, hand on own chin, jacket on shoulders, light smile, long sleeves, looking at viewer, looking up, medium breasts, office lady, smile, solo, suit, upper body, white shirt, outdoors",
    "1boy, male focus, gojou satoru, jujutsu kaisen, black jacket, blindfold lift, blue eyes, glowing, glowing eyes, high collar, jacket, jujutsu tech uniform, solo, grin, white hair",
    "1girl, cagliostro, granblue fantasy, violet eyes, standing, hand on own chin, looking at object, smile, closed mouth, table, beaker, glass tube, experiment apparatus, dark room, laboratory",
    "kimi no na wa., building, cityscape, cloud, cloudy sky, gradient sky, lens flare, no humans, outdoors, power lines, scenery, shooting star, sky, sparkle, star \(sky\), starry sky, sunset, tree, utility pole",
]

quality_prompt_list = [
    {
        "name": "(None)",
        "prompt": "{prompt}",
        "negative_prompt": "nsfw, lowres",
    },
    {
        "name": "Standard v3.0",
        "prompt": "{prompt}, masterpiece, best quality",
        "negative_prompt": "nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name",
    },
    {
        "name": "Standard v3.1",
        "prompt": "{prompt}, masterpiece, best quality, very aesthetic, absurdres",
        "negative_prompt": "nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]",
    },
    {
        "name": "Light v3.1",
        "prompt": "{prompt}, (masterpiece), best quality, very aesthetic, perfect face",
        "negative_prompt": "nsfw, (low quality, worst quality:1.2), very displeasing, 3d, watermark, signature, ugly, poorly drawn",
    },
    {
        "name": "Heavy v3.1",
        "prompt": "{prompt}, (masterpiece), (best quality), (ultra-detailed), very aesthetic, illustration, disheveled hair, perfect composition, moist skin, intricate details",
        "negative_prompt": "nsfw, longbody, lowres, bad anatomy, bad hands, missing fingers, pubic hair, extra digit, fewer digits, cropped, worst quality, low quality, very displeasing",
    },
]

sampler_list = [
    "DPM++ 2M Karras",
    "DPM++ SDE Karras",
    "DPM++ 2M SDE Karras",
    "Euler",
    "Euler a",
    "DDIM",
]

aspect_ratios = [
    "1024 x 1024",
    "1152 x 896",
    "896 x 1152",
    "1216 x 832",
    "832 x 1216",
    "1344 x 768",
    "768 x 1344",
    "1536 x 640",
    "640 x 1536",
    "Custom",
]

style_list = [
    {
        "name": "(None)",
        "prompt": "{prompt}",
        "negative_prompt": "",
    },
    {
        "name": "Cinematic",
        "prompt": "{prompt}, cinematic still, emotional, harmonious, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy",
        "negative_prompt": "nsfw, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured",
    },
    {
        "name": "Photographic",
        "prompt": "{prompt}, cinematic photo, 35mm photograph, film, bokeh, professional, 4k, highly detailed",
        "negative_prompt": "nsfw, drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly",
    },
    {
        "name": "Anime",
        "prompt": "{prompt}, anime artwork, anime style, key visual, vibrant, studio anime, highly detailed",
        "negative_prompt": "nsfw, photo, deformed, black and white, realism, disfigured, low contrast",
    },
    {
        "name": "Manga",
        "prompt": "{prompt}, manga style, vibrant, high-energy, detailed, iconic, Japanese comic style",
        "negative_prompt": "nsfw, ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, Western comic style",
    },
    {
        "name": "Digital Art",
        "prompt": "{prompt}, concept art, digital artwork, illustrative, painterly, matte painting, highly detailed",
        "negative_prompt": "nsfw, photo, photorealistic, realism, ugly",
    },
    {
        "name": "Pixel art",
        "prompt": "{prompt}, pixel-art, low-res, blocky, pixel art style, 8-bit graphics",
        "negative_prompt": "nsfw, sloppy, messy, blurry, noisy, highly detailed, ultra textured, photo, realistic",
    },
    {
        "name": "Fantasy art",
        "prompt": "{prompt}, ethereal fantasy concept art, magnificent, celestial, ethereal, painterly, epic, majestic, magical, fantasy art, cover art, dreamy",
        "negative_prompt": "nsfw, photographic, realistic, realism, 35mm film, dslr, cropped, frame, text, deformed, glitch, noise, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, sloppy, duplicate, mutated, black and white",
    },
    {
        "name": "Neonpunk",
        "prompt": "{prompt}, neonpunk style, cyberpunk, vaporwave, neon, vibes, vibrant, stunningly beautiful, crisp, detailed, sleek, ultramodern, magenta highlights, dark purple shadows, high contrast, cinematic, ultra detailed, intricate, professional",
        "negative_prompt": "nsfw, painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured",
    },
    {
        "name": "3D Model",
        "prompt": "{prompt}, professional 3d model, octane render, highly detailed, volumetric, dramatic lighting",
        "negative_prompt": "nsfw, ugly, deformed, noisy, low poly, blurry, painting",
    },
]