import Image from "next/image";
import Link from "next/link";
import bookCover from "../public/book-cover.webp";

const bookUrl =
  "https://www.routledge.com/Python-Scripting-for-PLAXIS-Automating-Geotechnical-Analysis-and-Modeling-Workflows/Akhtar/p/book/9781041245131";

const contactEmail = "w.akhtar@hotmail.com";

const navItems = [
  { label: "Home", href: "/" },
  { label: "About the Book", href: "#about" },
  { label: "Scripts", href: "#scripts" },
  { label: "Contact", href: "#contact" },
];

const bookTitle =
  "Python Scripting for PLAXIS: Automating Geotechnical Analysis and Modeling Workflows";

const aboutParagraphs = [
  "explores the integration of Python programming with geotechnical engineering to make numerical modelling and analysis more efficient, systematic, and automated.",
  "The book provides a practical approach to using Python for automating PLAXIS workflows, from model development and parameter definition to calculation management, results extraction, post-processing, and optimization. Through practical examples and scripting applications, it demonstrates how programming can help engineers streamline repetitive tasks, improve modelling efficiency, and develop more flexible and powerful numerical analysis workflows.",
  "Designed for geotechnical engineers, researchers, postgraduate students, and PLAXIS users, this book bridges the gap between conventional geotechnical engineering practice and computational methods. It encourages engineers to move beyond conventional software operations and explore the possibilities of programming-driven geotechnical analysis.",
  "Whether you are beginning your journey with Python or looking to advance your numerical modelling capabilities, this book provides a practical foundation for incorporating automation and computational techniques into geotechnical engineering.",
];

const scripts = [
  {
    file: "1_StaticPLT.py",
    title: "Static Pile Load Test",
    description:
      "Axisymmetric model with Mohr-Coulomb soil, loading/unloading stages, and pile head displacement curve.",
  },
  {
    file: "2_Dam_EQ.py",
    title: "Embankment Dam under Seismic Loading",
    description:
      "Plane strain model with zoned dam, earthquake accelerogram input, and crest acceleration time history.",
  },
  {
    file: "EQ.txt",
    title: "Earthquake Acceleration Record",
    description: "Input accelerogram used by the embankment dam example.",
  },
  {
    file: "3_Tunnel.py",
    title: "Tunnel Excavation and Support Design",
    description:
      "Plane strain model with Hoek-Brown rock, shotcrete lining, rock bolts, and crown/wall displacement curves.",
  },
  {
    file: "4_Slopestability.py",
    title: "Slope Stability Analysis",
    description:
      "Bench-cut slope in Hoek-Brown rock using the strength reduction method with Factor of Safety curve.",
  },
];

const sectionClass =
  "scroll-mt-20 border-t border-slate-800 px-6 py-16 sm:py-20";
const headingClass = "text-2xl sm:text-3xl font-bold tracking-tight text-white";

function PythonLogo({ className }: { className?: string }) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 110 110"
      className={className}
      aria-label="Python logo"
    >
      <defs>
        <linearGradient id="pyBlue" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#5A9FD4" />
          <stop offset="100%" stopColor="#306998" />
        </linearGradient>
        <linearGradient id="pyYellow" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#FFD43B" />
          <stop offset="100%" stopColor="#FFE873" />
        </linearGradient>
      </defs>
      <path
        d="M54.9 3.3c-26.1 0-24.5 11.3-24.5 11.3l.03 11.7h24.9v3.5H21.6S3.3 27.5 3.3 54.1s16 25.7 16 25.7h9.5V67.9s-.5-16 15.8-16h27.1s15.2.2 15.2-14.7V16.4S89.6 3.3 54.9 3.3zM40.1 11.3a4.9 4.9 0 1 1 0 9.8 4.9 4.9 0 0 1 0-9.8z"
        fill="url(#pyBlue)"
      />
      <path
        d="M55.1 106.7c26.1 0 24.5-11.3 24.5-11.3l-.03-11.7H54.6v-3.5h33.7s18.3 2.3 18.3-24.3-16-25.7-16-25.7h-9.5v11.9s.5 16-15.8 16H38.2s-15.2-.2-15.2 14.7v20.8s-2.7 13.1 32 13.1zm14.8-8a4.9 4.9 0 1 1 0-9.8 4.9 4.9 0 0 1 0 9.8z"
        fill="url(#pyYellow)"
      />
    </svg>
  );
}

function PlaxisLogo({ className }: { className?: string }) {
  return (
    <Image
      src={`${process.env.NEXT_PUBLIC_BASE_PATH}/plaxis-logo.svg`}
      alt="PLAXIS logo"
      width={520}
      height={174}
      className={className}
    />
  );
}

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col">
      {/* Navigation */}
      <nav className="border-b border-slate-700/50 backdrop-blur-sm bg-slate-900/80 sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <span className="text-sm font-mono font-semibold text-amber-400 tracking-wide">
            PythonforPLAXIS
          </span>
          <ul className="hidden md:flex items-center gap-8">
            {navItems.map((item) => (
              <li key={item.label}>
                <Link
                  href={item.href}
                  className="text-sm text-slate-400 hover:text-white transition-colors"
                >
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
          <a
            href="https://github.com/geotechscripting/PythonforPLAXIS"
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm text-slate-400 hover:text-white transition-colors"
          >
            GitHub
          </a>
        </div>
      </nav>

      {/* Hero */}
      <main className="flex-1 flex flex-col items-center justify-center px-6 pt-24 pb-16">
        <div className="max-w-3xl mx-auto text-center space-y-8 -mt-16">
          {/* Logos */}
          <div className="flex items-center justify-center gap-6">
            <PythonLogo className="h-20 w-20 sm:h-24 sm:w-24" />
            <span className="text-3xl text-slate-600 font-light select-none">
              +
            </span>
            <PlaxisLogo className="h-12 w-auto sm:h-14" />
          </div>

          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-white leading-tight">
            Python Scripting
            <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-orange-500">
              for PLAXIS
            </span>
          </h1>

          <p className="text-lg sm:text-xl text-slate-400 max-w-2xl mx-auto leading-relaxed">
            Automating Geotechnical Analysis and Modeling Workflows
          </p>

          <a
            href={bookUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="block w-48 sm:w-60 mx-auto transition-transform hover:scale-[1.02]"
          >
            <Image
              src={bookCover}
              alt="Cover of Python Scripting for PLAXIS"
              className="w-full h-auto rounded-md shadow-2xl shadow-black/50"
              priority
            />
          </a>

          <div className="w-16 h-px bg-gradient-to-r from-transparent via-slate-600 to-transparent mx-auto"></div>

          <p className="text-sm text-slate-500 max-w-lg mx-auto">
            Companion website for the book.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
            <a
              href="https://github.com/geotechscripting/PythonforPLAXIS"
              target="_blank"
              rel="noopener noreferrer"
              className="rounded-lg bg-white text-slate-900 px-6 py-3 text-sm font-semibold hover:bg-slate-200 transition-colors"
            >
              View on GitHub
            </a>
            <a
              href={bookUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="rounded-lg border border-slate-700 px-6 py-3 text-sm text-slate-300 hover:border-slate-500 hover:text-white transition-colors"
            >
              Get the Book
            </a>
          </div>
        </div>
      </main>

      {/* About the Book */}
      <section id="about" className={sectionClass}>
        <div className="max-w-3xl mx-auto space-y-6">
          <h2 className={headingClass}>About the Book</h2>
          {aboutParagraphs.map((text, i) => (
            <p key={i} className="text-slate-400 leading-relaxed">
              {i === 0 && (
                <span className="font-medium text-slate-200">{bookTitle} </span>
              )}
              {text}
            </p>
          ))}
        </div>
      </section>

      {/* Scripts */}
      <section id="scripts" className={sectionClass}>
        <div className="max-w-3xl mx-auto space-y-6">
          <h2 className={headingClass}>Scripts</h2>
          <p className="text-slate-400 leading-relaxed">
            Example scripts from the book. Each requires PLAXIS 2D with the
            Remote Scripting Server enabled; update the port numbers and
            password to match your configuration.
          </p>
          <ul className="divide-y divide-slate-800 rounded-lg border border-slate-800">
            {scripts.map((s) => (
              <li
                key={s.file}
                className="flex flex-col sm:flex-row sm:items-center gap-3 sm:gap-6 p-4 sm:p-5"
              >
                <div className="flex-1 space-y-1">
                  <p className="font-semibold text-white">{s.title}</p>
                  <p className="text-sm text-slate-400">{s.description}</p>
                  <p className="text-xs font-mono text-amber-400/80">
                    {s.file}
                  </p>
                </div>
                <a
                  href={`${process.env.NEXT_PUBLIC_BASE_PATH}/scripts/${s.file}`}
                  download
                  className="self-start sm:self-center rounded-lg border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:border-slate-500 hover:text-white transition-colors"
                >
                  Download
                </a>
              </li>
            ))}
          </ul>
        </div>
      </section>

      {/* Contact */}
      <section id="contact" className={sectionClass}>
        <div className="max-w-3xl mx-auto space-y-4">
          <h2 className={headingClass}>Contact</h2>
          <p className="text-slate-400 leading-relaxed">
            Questions or feedback about the book or scripts? Contact the author,
            Waseem Akhtar, at{" "}
            <a
              href={`mailto:${contactEmail}`}
              className="text-amber-400 hover:text-amber-300 transition-colors"
            >
              {contactEmail}
            </a>
            .
          </p>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-800 py-6 px-6 text-center space-y-2">
        <p className="text-xs text-slate-600">
          &copy; {new Date().getFullYear()} geotechscripting
        </p>
        <p className="text-[10px] text-slate-700 max-w-xl mx-auto leading-relaxed">
          Python and the Python logo are trademarks of the Python Software
          Foundation. PLAXIS is a registered trademark of Bentley Systems,
          Incorporated. This website is not affiliated with or endorsed by the
          Python Software Foundation or Bentley Systems.
        </p>
      </footer>
    </div>
  );
}
