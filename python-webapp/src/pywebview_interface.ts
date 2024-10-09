declare global {
    interface Window {
      pywebview: {
        api: {
          [key: string]: (...args: unknown[]) => Promise<unknown>;
        };
        [key: string]: unknown;
      };
    }
  }