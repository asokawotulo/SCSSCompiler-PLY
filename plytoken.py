import re

tokens = (
	"SINGLE_COMMENT", "MULTI_COMMENT",
	"DEC_VARIABLE", "CALL_VARIABLE", 
	"URLS",
	"CLASS", "ID", "PARENT_REF", "ELEMENT", "PSEUDO_ELEMENT", "ATTRI_ELEMENT",
	"PROPERTY",
	"COLON", "SEMICOLON", "LCURLY", "RCURLY",
	"HEX", "VALUE", "UNITS", "COMMA"
)

# Tokens
# ROOT
t_ignore_SINGLE_COMMENT = r'//.*?\n'
t_MULTI_COMMENT         = r'/\*[\s\w]*?\*/'
t_DEC_VARIABLE          = r'(\$[\w][\w-]*\s*:)'
t_CALL_VARIABLE         = r'\s*(\$[\w][\w-]*)'
# OPERATORS
t_COMMA                 = r'\s*,\s*'
t_RCURLY                = r'}'
t_COLON                 = r':'
t_SEMICOLON             = r';'
t_LCURLY                = r'{'
# CONTENT
t_CLASS                 = r'\.[a-zA-Z0-9_-]+'
t_ID                    = r'\#[a-zA-Z0-9_-]+'
t_PARENT_REF            = r'&[a-zA-Z0-9_-]+'
t_ELEMENT               = r'(\*|html|body|div|span|applet|object|iframe|h1|h2|h3|h4|h5|h6|p|blockquote|pre|a|abbr|acronym|address|big|cite|code|del|dfn|em|img|ins|kbd|q|s|samp|small|strike|strong|sub|sup|tt|var|ol|ul|li|dl|dt|dd|fieldset|form|label|legend|table|caption|tbody|tfoot|thead|tr|th|td|article|aside|canvas|details|embed|figure|figcaption|footer|header|hgroup|menu|nav|output|ruby|section|summary|time|mark|audio|video|article|aside|details|figcaption|figure|footer|header|hgroup|menu|nav|section|body|ol|ul|blockquote|q|blockquote|blockquote|q|q|table)'
t_PSEUDO_ELEMENT        = r'(' + t_PARENT_REF + r'|' + t_CLASS + r'|' + t_ID + r'|' + t_ELEMENT + r')' + r'(:|::)[a-zA-Z0-9_-]+'
t_ATTRI_ELEMENT         = r'(' + t_PARENT_REF + r'|' + t_CLASS + r'|' + t_ID + r'|' + t_ELEMENT + r')' + r'\[[\w=\'\"]+\]'
t_URLS                  = r'\s*(url)\([a-zA-Z0-9-_\'\"\.\/]+\)'
t_PROPERTY              = r'(azimuth|align-items|background-attachment|background-color|background-image|background-position|background-repeat|background-size|background|border-bottom-color|border-bottom-style|border-bottom-width|border-left-color|border-left-style|border-left-width|border-right|border-right-color|border-right-style|border-right-width|border-top-color|border-top-style|border-top-width|border-bottom|border-collapse|border-left|border-width|border-color|border-spacing|border-style|border-top|border|caption-side|clear|clip|color|content|counter-increment|counter-reset|cue-after|cue-before|cue|cursor|direction|display|elevation|empty-cells|float|font-family|font-size|font-size-adjust|font-stretch|font-style|font-variant|font-weight|font|flex-wrap|flex-direction|flex-basis|flex-flow|flex-grow|height|letter-spacing|line-height|list-style-type|list-style-image|list-style-position|list-style|margin-bottom|margin-left|margin-right|margin-top|margin|marker-offset|marks|max-height|max-width|min-height|min-width|opacity|orphans|outline|outline-color|outline-style|outline-width|overflow|padding-bottom|padding-left|padding-right|padding-top|padding|page|page-break-after|page-break-before|page-break-inside|pause-after|pause-before|pause|pitch|pitch-range|play-during|position|quotes|richness|right|size|speak-header|speak-numeral|speak-punctuation|speak|speech-rate|stress|table-layout|text-align|text-decoration|text-indent|text-shadow|text-transform|top|unicode-bidi|vertical-align|visibility|voice-family|volume|white-space|widows|width|word-spacing|z-index|bottom|left|above|absolute|always|armenian|aural|auto|avoid|baseline|behind|below|bidi-override|blink|bold|bolder|both|capitalize|circle|cjk-ideographic|close-quote|collapse|condensed|continuous|crop|crosshair|cross|cursive|dashed|decimal-leading-zero|decimal|default|digits|disc|dotted|double|e-resize|embed|extra-condensed|extra-expanded|expanded|fantasy|far-left|far-right|faster|fast|fixed|georgian|groove|hebrew|help|hidden|hide|higher|high|hiragana-iroha|hiragana|icon|inherit|inset|inside|invert|italic|justify-content|katakana-iroha|katakana|landscape|larger|large|left-side|leftwards|level|lighter|line-through|list-item|loud|lower-alpha|lower-greek|lower-roman|lowercase|ltr|lower|low|medium|message-box|middle|mix|monospace|n-resize|narrower|ne-resize|no-close-quote|no-open-quote|no-repeat|normal|nowrap|nw-resize|oblique|once|open-quote|outset|outside|overline|pointer|portrait|px|relative|repeat-x|repeat-y|repeat|rgb|ridge|right-side|rightwards|s-resize|sans-serif|scroll|se-resize|semi-condensed|semi-expanded|separate|serif|show|silent|slow|slower|small-caps|small-caption|smaller|soft|solid|spell-out|square|static|status-bar|super|sw-resize|table-caption|table-cell|table-column|table-column-group|table-footer-group|table-header-group|table-row|table-row-group|text|text-bottom|text-top|thick|thin|transparent|ultra-condensed|ultra-expanded|underline|visible|w-resize|wait|wider|x-fast|x-high|x-large|x-loud|x-low|x-small|x-soft|xx-large|xx-small)\b'
# t_KEY_COLOR             = r'(indigo|gold|firebrick|indianred|yellow|darkolivegreen|darkseagreen|mediumvioletred|mediumorchid|chartreuse|mediumslateblue|black|springgreen|crimson|lightsalmon|brown|turquoise|olivedrab|cyan|silver|skyblue|gray|darkturquoise|goldenrod|darkgreen|darkviolet|darkgray|lightpink|teal|darkmagenta|lightgoldenrodyellow|lavender|yellowgreen|thistle|violet|navy|orchid|blue|ghostwhite|honeydew|cornflowerblue|darkblue|darkkhaki|mediumpurple|cornsilk|red|bisque|slategray|darkcyan|khaki|wheat|deepskyblue|darkred|steelblue|aliceblue|gainsboro|mediumturquoise|floralwhite|coral|purple|lightgrey|lightcyan|darksalmon|beige|azure|lightsteelblue|oldlace|greenyellow|royalblue|lightseagreen|mistyrose|sienna|lightcoral|orangered|navajowhite|lime|palegreen|burlywood|seashell|mediumspringgreen|fuchsia|papayawhip|blanchedalmond|peru|aquamarine|white|darkslategray|ivory|dodgerblue|lemonchiffon|chocolate|orange|forestgreen|slateblue|olive|mintcream|antiquewhite|darkorange|cadetblue|moccasin|limegreen|saddlebrown|darkslateblue|lightskyblue|deeppink|plum|aqua|darkgoldenrod|maroon|sandybrown|magenta|tan|rosybrown|pink|lightblue|palevioletred|mediumseagreen|dimgray|powderblue|seagreen|snow|mediumblue|midnightblue|paleturquoise|palegoldenrod|whitesmoke|darkorchid|salmon|lightslategray|lawngreen|lightgreen|tomato|hotpink|lightyellow|lavenderblush|linen|mediumaquamarine|green|blueviolet|peachpuff|black|silver|gray|white|maroon|red|purple|fuchsia|green|lime|olive|yellow|navy|blue|teal|aqua)\b'
# VALUES
t_HEX                   = r'\s*\#[a-fA-F0-9]{1,6}'
absolute                = r'in|cm|mm|pc|pt|px'
relative                = r'em|rem|vw|vh|vmin|vmax|%'
angular                 = r'deg|grad|rad|turn'
time                    = r's|ms'
frequency               = r'Hz|kHz'
resolution              = r'dpi|dpcm|dppx'
t_UNITS                 = r'\s*[0-9]?\.?[0-9]+(' + relative + r'|' + absolute + r'|' + angular + r'|' + time + r'|' + frequency + r'|' + resolution + r')?'
t_VALUE                 = r'[a-zA-Z\s-]+'

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def find_column(data, token):
	line_start = data.rfind('\n', 0, token.lexpos) + 1
	return (token.lexpos - line_start) + 1

# Ignored characters
t_ignore = "\t "

def t_error(t):
	print("Syntax Error on {}:{}".format(t.lineno, find_column(source_text, t)))
	t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()