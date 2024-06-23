import os

# Create the project directories
os.makedirs('book_project/config', exist_ok=True)
os.makedirs('book_project/chapters', exist_ok=True)

# Create preamble.tex
with open('book_project/config/preamble.tex', 'w', encoding='utf-8') as file:
    file.write(r"""
% Preamble for the Arabic book

% Use the fancyhdr package for custom headers
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\nouppercase{\rightmark}}
\fancyhead[RO]{\nouppercase{\leftmark}}
\fancyfoot[C]{\thepage}

% Use the polyglossia package for better support of Arabic
\usepackage{polyglossia}
\setdefaultlanguage{arabic}
\setotherlanguage{english}

% Set the main font to an appropriate Arabic font
\newfontfamily\arabicfont[Script=Arabic]{Amiri}
\newfontfamily\arabicfonttt[Script=Arabic]{Amiri}

% Redefine the chapter command to align to the right and remove numbering
\makeatletter
\renewcommand{\@makechapterhead}[1]{
  \vspace*{50\p@}
  {\parindent \z@ \raggedleft \normalfont
    \interlinepenalty\@M
    \Huge \bfseries #1\par\nobreak
    \vskip 40\p@
  }
  \markboth{#1}{}
}
\makeatother

% Redefine section numbering to use English numerals and include chapter number
\renewcommand{\thesection}{\thechapter.\arabic{section}}

% Ensure page numbers use Arabic numerals
\renewcommand{\thepage}{\arabic{page}}
""")

# Create Chapter00.tex with introduction
with open('book_project/chapters/Chapter00.tex', 'w', encoding='utf-8') as file:
    file.write(r"""
\chapter{مقدمة}

محتوى المقدمة هنا. هذا النص هو مجرد نص تجريبي لإظهار كيف يبدو النص العربي في كتاب لاتيكس.
""")

# Create Chapter01.tex with content
with open('book_project/chapters/Chapter01.tex', 'w', encoding='utf-8') as file:
    file.write(r"""
\chapter{الفصل الأول}

\section{مقدمة}
هذه هي المقدمة للفصل الأول.

\section{معادلات}
فيما يلي مثال على معادلة رياضية:

\begin{equation}
E = mc^2
\end{equation}

ومثال آخر على معادلة معقدة:

\begin{equation}
\int_0^\infty e^{-x^2} \, dx = \frac{\sqrt{\pi}}{2}
\end{equation}

\newpage

\section{نص الفصل الأول - الصفحة الثانية}

هذه الصفحة الثانية للفصل الأول تحتوي على نص إضافي لتوضيح كيفية تنسيق النصوص في كتب اللاتكس باللغة العربية.

\newpage

\section{نص الفصل الأول - الصفحة الثالثة}

هذه الصفحة الثالثة للفصل الأول تحتوي على المزيد من النصوص لاختبار تقسيم الصفحات وظهور الرؤوس والأقدام بشكل صحيح في النصوص العربية.
""")

# Create Chapter02.tex with content
with open('book_project/chapters/Chapter02.tex', 'w', encoding='utf-8') as file:
    file.write(r"""
\chapter{الفصل الثاني}

\section{جداول}
فيما يلي مثال على جدول:

\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|}
\hline
العنوان 1 & العنوان 2 & العنوان 3 \\
\hline
الخلية 1 & الخلية 2 & الخلية 3 \\
\hline
الخلية 4 & الخلية 5 & الخلية 6 \\
\hline
\end{tabular}
\caption{مثال على جدول}
\end{table}

\newpage

\section{مراجع}
يمكنك إضافة مراجع كما يلي:

\begin{itemize}
    \item المرجع الأول
    \item المرجع الثاني
    \item المرجع الثالث
\end{itemize}

% Example of a reference using BibTeX
\section{مراجع باستخدام BibTeX}
لإضافة مراجع باستخدام BibTeX، يمكن استخدام الملف التالي `references.bib`:

\begin{verbatim}
@book{example,
  author    = "المؤلف",
  title     = "عنوان الكتاب",
  publisher = "دار النشر",
  year      = "السنة"
}
\end{verbatim}

ثم تضمين المراجع في المستند الرئيسي:

\begin{verbatim}
\bibliographystyle{plain}
\bibliography{references}
\end{verbatim}

\newpage

\section{نص الفصل الثاني - الصفحة الثانية}

هذه الصفحة الثانية للفصل الثاني تحتوي على نص إضافي لاختبار تقسيم الصفحات وظهور الرؤوس والأقدام بشكل صحيح في النصوص العربية.

\newpage

\section{نص الفصل الثاني - الصفحة الثالثة}

هذه الصفحة الثالثة للفصل الثاني تحتوي على المزيد من النصوص لاختبار تقسيم الصفحات وظهور الرؤوس والأقدام بشكل صحيح في النصوص العربية.
""")

# Create main.tex
with open('book_project/main.tex', 'w', encoding='utf-8') as file:
    file.write(r"""
\documentclass[14pt]{book}
\usepackage[a5paper,top=1in,bottom=1in,left=0.75in,right=0.75in]{geometry}

% Include the preamble
\input{config/preamble.tex}

% Title of the book
\title{حساب}
\author{المؤلف}
\date{}

\begin{document}

\maketitle
\tableofcontents

% Include Chapter00
\input{chapters/Chapter00.tex}

% Include chapters
\input{chapters/Chapter01.tex}
\input{chapters/Chapter02.tex}

% Include references (if using BibTeX)
\bibliographystyle{plain}
\bibliography{references}

\end{document}
""")

# Create references.bib
with open('book_project/references.bib', 'w', encoding='utf-8') as file:
    file.write(r"""
@book{example,
  author    = "المؤلف",
  title     = "عنوان الكتاب",
  publisher = "دار النشر",
  year      = "السنة"
}
""")
