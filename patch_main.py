import re

with open('/var/www/html/zazi/zazinuxt/public/js/main.js', 'r') as f:
    content = f.read()

# Patch 07. Hero Slider Active
hero_pattern = r'(/\*----------- 07\. Hero Slider Active ----------\*/\s*)(\$\("\.vs-hero-carousel"\)\.each\(function \(\) \{)'
hero_repl = r'\1window.initHeroSlider = function() {\n    \2\n      if ($(this).hasClass("ls-container")) return;'
content = re.sub(hero_pattern, hero_repl, content)

# We need to close the function
# The block ends before /*----------- 08. Global Slider ----------*/
end_hero_pattern = r'(    \}\);\n  \}\);\n)(\s*/\*----------- 08\. Global Slider ----------\*/)'
end_hero_repl = r'    });\n  };\n  window.initHeroSlider();\n\2'
content = re.sub(end_hero_pattern, end_hero_repl, content)

# Patch 08. Global Slider
global_pattern = r'(/\*----------- 08\. Global Slider ----------\*/\s*)(\$\("\.vs-carousel"\)\.each\(function \(\) \{)'
global_repl = r'\1window.initGlobalSlider = function() {\n    \2\n      if ($(this).hasClass("slick-initialized")) return;'
content = re.sub(global_pattern, global_repl, content)

# The block ends before /*----------- 09. Ajax Contact Form ----------*/
end_global_pattern = r'(      \],\n    \}\);\n  \}\);\n)(\s*/\*----------- 09\. Ajax Contact Form ----------\*/)'
end_global_repl = r'      ],\n    });\n  });\n  };\n  window.initGlobalSlider();\n\2'
content = re.sub(end_global_pattern, end_global_repl, content)

with open('/var/www/html/zazi/zazinuxt/public/js/main.js', 'w') as f:
    f.write(content)

print("Patch applied")
