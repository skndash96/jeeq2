
// this file is generated — do not edit it


/// <reference types="@sveltejs/kit" />

/**
 * Environment variables [loaded by Vite](https://vitejs.dev/guide/env-and-mode.html#env-files) from `.env` files and `process.env`. Like [`$env/dynamic/private`](https://kit.svelte.dev/docs/modules#$env-dynamic-private), this module cannot be imported into client-side code. This module only includes variables that _do not_ begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env) _and do_ start with [`config.kit.env.privatePrefix`](https://kit.svelte.dev/docs/configuration#env) (if configured).
 * 
 * _Unlike_ [`$env/dynamic/private`](https://kit.svelte.dev/docs/modules#$env-dynamic-private), the values exported from this module are statically injected into your bundle at build time, enabling optimisations like dead code elimination.
 * 
 * ```ts
 * import { API_KEY } from '$env/static/private';
 * ```
 * 
 * Note that all environment variables referenced in your code should be declared (for example in an `.env` file), even if they don't have a value until the app is deployed:
 * 
 * ```
 * MY_FEATURE_FLAG=""
 * ```
 * 
 * You can override `.env` values from the command line like so:
 * 
 * ```bash
 * MY_FEATURE_FLAG="enabled" npm run dev
 * ```
 */
declare module '$env/static/private' {
	export const DEX2OATBOOTCLASSPATH: string;
	export const TERMUX_MAIN_PACKAGE_FORMAT: string;
	export const npm_config_version_commit_hooks: string;
	export const npm_config_user_agent: string;
	export const EXTERNAL_STORAGE: string;
	export const npm_config_bin_links: string;
	export const npm_node_execpath: string;
	export const npm_package_devDependencies_vite: string;
	export const npm_config_init_version: string;
	export const SHLVL: string;
	export const HOME: string;
	export const OLDPWD: string;
	export const npm_config_init_license: string;
	export const YARN_WRAP_OUTPUT: string;
	export const npm_config_version_tag_prefix: string;
	export const npm_package_devDependencies__fontsource_fira_mono: string;
	export const BOOTCLASSPATH: string;
	export const npm_config_engine_strict: string;
	export const npm_config_resolution_mode: string;
	export const COLORTERM: string;
	export const npm_package_readmeFilename: string;
	export const TMPDIR: string;
	export const npm_package_scripts_dev: string;
	export const npm_package_type: string;
	export const _: string;
	export const npm_config_registry: string;
	export const TERM: string;
	export const ANDROID_DATA: string;
	export const npm_config_ignore_scripts: string;
	export const HISTCONTROL: string;
	export const PATH: string;
	export const NODE: string;
	export const npm_package_name: string;
	export const ANDROID_I18N_ROOT: string;
	export const ANDROID_ROOT: string;
	export const LD_PRELOAD: string;
	export const LANG: string;
	export const npm_lifecycle_script: string;
	export const PREFIX: string;
	export const npm_package_devDependencies__sveltejs_kit: string;
	export const npm_config_version_git_message: string;
	export const SHELL: string;
	export const ANDROID_TZDATA_ROOT: string;
	export const npm_lifecycle_event: string;
	export const npm_package_version: string;
	export const npm_config_argv: string;
	export const npm_package_devDependencies_svelte: string;
	export const npm_package_scripts_build: string;
	export const npm_config_foreground_scripts: string;
	export const npm_config_version_git_tag: string;
	export const npm_config_version_git_sign: string;
	export const npm_config_strict_ssl: string;
	export const PWD: string;
	export const npm_execpath: string;
	export const npm_package_devDependencies__sveltejs_adapter_auto: string;
	export const npm_package_devDependencies__neoconfetti_svelte: string;
	export const npm_config_save_prefix: string;
	export const npm_config_ignore_optional: string;
	export const ANDROID_ART_ROOT: string;
	export const npm_package_scripts_preview: string;
	export const INIT_CWD: string;
	export const NODE_ENV: string;
}

/**
 * Similar to [`$env/static/private`](https://kit.svelte.dev/docs/modules#$env-static-private), except that it only includes environment variables that begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env) (which defaults to `PUBLIC_`), and can therefore safely be exposed to client-side code.
 * 
 * Values are replaced statically at build time.
 * 
 * ```ts
 * import { PUBLIC_BASE_URL } from '$env/static/public';
 * ```
 */
declare module '$env/static/public' {
	
}

/**
 * This module provides access to runtime environment variables, as defined by the platform you're running on. For example if you're using [`adapter-node`](https://github.com/sveltejs/kit/tree/master/packages/adapter-node) (or running [`vite preview`](https://kit.svelte.dev/docs/cli)), this is equivalent to `process.env`. This module only includes variables that _do not_ begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env) _and do_ start with [`config.kit.env.privatePrefix`](https://kit.svelte.dev/docs/configuration#env) (if configured).
 * 
 * This module cannot be imported into client-side code.
 * 
 * ```ts
 * import { env } from '$env/dynamic/private';
 * console.log(env.DEPLOYMENT_SPECIFIC_VARIABLE);
 * ```
 * 
 * > In `dev`, `$env/dynamic` always includes environment variables from `.env`. In `prod`, this behavior will depend on your adapter.
 */
declare module '$env/dynamic/private' {
	export const env: {
		DEX2OATBOOTCLASSPATH: string;
		TERMUX_MAIN_PACKAGE_FORMAT: string;
		npm_config_version_commit_hooks: string;
		npm_config_user_agent: string;
		EXTERNAL_STORAGE: string;
		npm_config_bin_links: string;
		npm_node_execpath: string;
		npm_package_devDependencies_vite: string;
		npm_config_init_version: string;
		SHLVL: string;
		HOME: string;
		OLDPWD: string;
		npm_config_init_license: string;
		YARN_WRAP_OUTPUT: string;
		npm_config_version_tag_prefix: string;
		npm_package_devDependencies__fontsource_fira_mono: string;
		BOOTCLASSPATH: string;
		npm_config_engine_strict: string;
		npm_config_resolution_mode: string;
		COLORTERM: string;
		npm_package_readmeFilename: string;
		TMPDIR: string;
		npm_package_scripts_dev: string;
		npm_package_type: string;
		_: string;
		npm_config_registry: string;
		TERM: string;
		ANDROID_DATA: string;
		npm_config_ignore_scripts: string;
		HISTCONTROL: string;
		PATH: string;
		NODE: string;
		npm_package_name: string;
		ANDROID_I18N_ROOT: string;
		ANDROID_ROOT: string;
		LD_PRELOAD: string;
		LANG: string;
		npm_lifecycle_script: string;
		PREFIX: string;
		npm_package_devDependencies__sveltejs_kit: string;
		npm_config_version_git_message: string;
		SHELL: string;
		ANDROID_TZDATA_ROOT: string;
		npm_lifecycle_event: string;
		npm_package_version: string;
		npm_config_argv: string;
		npm_package_devDependencies_svelte: string;
		npm_package_scripts_build: string;
		npm_config_foreground_scripts: string;
		npm_config_version_git_tag: string;
		npm_config_version_git_sign: string;
		npm_config_strict_ssl: string;
		PWD: string;
		npm_execpath: string;
		npm_package_devDependencies__sveltejs_adapter_auto: string;
		npm_package_devDependencies__neoconfetti_svelte: string;
		npm_config_save_prefix: string;
		npm_config_ignore_optional: string;
		ANDROID_ART_ROOT: string;
		npm_package_scripts_preview: string;
		INIT_CWD: string;
		NODE_ENV: string;
		[key: `PUBLIC_${string}`]: undefined;
		[key: `${string}`]: string | undefined;
	}
}

/**
 * Similar to [`$env/dynamic/private`](https://kit.svelte.dev/docs/modules#$env-dynamic-private), but only includes variables that begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env) (which defaults to `PUBLIC_`), and can therefore safely be exposed to client-side code.
 * 
 * Note that public dynamic environment variables must all be sent from the server to the client, causing larger network requests — when possible, use `$env/static/public` instead.
 * 
 * ```ts
 * import { env } from '$env/dynamic/public';
 * console.log(env.PUBLIC_DEPLOYMENT_SPECIFIC_VARIABLE);
 * ```
 */
declare module '$env/dynamic/public' {
	export const env: {
		[key: `PUBLIC_${string}`]: string | undefined;
	}
}
