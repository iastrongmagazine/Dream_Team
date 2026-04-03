"use client";

export function NewsletterForm() {
  return (
    <form className="flex w-full max-w-sm gap-2" onSubmit={(e) => e.preventDefault()}>
      <input
        type="email"
        placeholder="tu@email.com"
        className="flex-1 rounded-md border border-white/20 bg-white/10 px-3 py-2 text-sm text-white placeholder:text-white/40 focus:outline-none focus:ring-2 focus:ring-secondary"
      />
      <button
        type="submit"
        className="rounded-md bg-secondary px-4 py-2 text-sm font-medium text-primary-dark hover:bg-secondary-light transition-colors"
      >
        Suscribir
      </button>
    </form>
  );
}
