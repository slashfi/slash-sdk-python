# Changelog

## 0.1.0-alpha.3 (2026-03-06)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/slashfi/slash-sdk-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** api update ([800f4fc](https://github.com/slashfi/slash-sdk-python/commit/800f4fcf172d2c11b5d4b10dbfb4a463d52ed6cb))

## 0.1.0-alpha.2 (2026-03-06)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/slashfi/slash-sdk-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* clean up environment call outs ([4ad1004](https://github.com/slashfi/slash-sdk-python/commit/4ad1004bad56af213217d78141a25c50cefb42a2))
* **client:** add follow_redirects request option ([9df418b](https://github.com/slashfi/slash-sdk-python/commit/9df418b9d18347bf14f4ed4f4dbca5db3feaf521))
* **client:** add support for aiohttp ([3eb209f](https://github.com/slashfi/slash-sdk-python/commit/3eb209fa3e453273442b521aab466f9df9b73fa5))


### Bug Fixes

* **ci:** correct conditional ([68884e8](https://github.com/slashfi/slash-sdk-python/commit/68884e8986638113fbbad9acbc30cdf234164618))
* **ci:** release-doctor — report correct token name ([68d96ff](https://github.com/slashfi/slash-sdk-python/commit/68d96ff71da2be9c21a075bd367f70ea045f2fb8))
* **client:** correctly parse binary response | stream ([539d6bf](https://github.com/slashfi/slash-sdk-python/commit/539d6bf673de7c5e22e91cf3c772d549c91b2e03))
* **client:** don't send Content-Type header on GET requests ([51bb320](https://github.com/slashfi/slash-sdk-python/commit/51bb32045c91c5012d612042cd1651f00757e588))
* **parsing:** correctly handle nested discriminated unions ([51edf3f](https://github.com/slashfi/slash-sdk-python/commit/51edf3f3aa2531739c8b8e221dae573cbb187b4c))
* **parsing:** ignore empty metadata ([85b43fb](https://github.com/slashfi/slash-sdk-python/commit/85b43fb287242201157d2802498929eff6964266))
* **parsing:** parse extra field types ([0f75cf3](https://github.com/slashfi/slash-sdk-python/commit/0f75cf32099a0a2f62e4bedfa486652df6bbce93))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([e0ac852](https://github.com/slashfi/slash-sdk-python/commit/e0ac852222cd61422abaaf500fa7c4bef0db3337))


### Chores

* **ci:** change upload type ([81e0486](https://github.com/slashfi/slash-sdk-python/commit/81e04862374726575980dc33acbb30bc4ecfccb8))
* **ci:** enable for pull requests ([cc425b5](https://github.com/slashfi/slash-sdk-python/commit/cc425b5b5d46fd3af23dbfacc61da8a8856c9d5e))
* **ci:** only run for pushes and fork pull requests ([91e27a2](https://github.com/slashfi/slash-sdk-python/commit/91e27a29542b197e2909d61ea8c2cae7b2755cb8))
* configure new SDK language ([1eae2cb](https://github.com/slashfi/slash-sdk-python/commit/1eae2cbc76e8ff3bdd5e10cb75573879646278c0))
* **docs:** remove reference to rye shell ([d745025](https://github.com/slashfi/slash-sdk-python/commit/d74502525553bb9c7374e4300c3c920bcc78bc3c))
* **docs:** remove unnecessary param examples ([0673d97](https://github.com/slashfi/slash-sdk-python/commit/0673d9730b1128fbaed1d143e2f573843f0c13e0))
* **internal:** bump pinned h11 dep ([721cd0c](https://github.com/slashfi/slash-sdk-python/commit/721cd0ce8f3bc83d7f4016c1418db849b41987d7))
* **internal:** codegen related update ([eb41b78](https://github.com/slashfi/slash-sdk-python/commit/eb41b787a0cb2f29ea863eb0cb9f767c6c95e7cd))
* **internal:** update conftest.py ([bfbab5c](https://github.com/slashfi/slash-sdk-python/commit/bfbab5ca00ff7a3800bc3a19c17f60556237c648))
* **package:** mark python 3.13 as supported ([6cc8a38](https://github.com/slashfi/slash-sdk-python/commit/6cc8a3889ccc88587b7738c73e2be2f6a24a056e))
* **readme:** fix version rendering on pypi ([7f5d547](https://github.com/slashfi/slash-sdk-python/commit/7f5d547e17b548a02ae09be29668d5015a2d22ce))
* **readme:** update badges ([a32bd73](https://github.com/slashfi/slash-sdk-python/commit/a32bd7368002955f1a0cc2412a4ece9e52aa159f))
* **tests:** add tests for httpx client instantiation & proxies ([8852f4b](https://github.com/slashfi/slash-sdk-python/commit/8852f4bb22390c1f3fb9dfd1542d59fce8d3fd70))
* **tests:** run tests in parallel ([02ad96f](https://github.com/slashfi/slash-sdk-python/commit/02ad96f0f240fc3a66e8b37b6360957100c26d0c))
* **tests:** skip some failing tests on the latest python versions ([6b36079](https://github.com/slashfi/slash-sdk-python/commit/6b36079b93a5e4c4ca0d1a38ed9336ab4b8687fd))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([f3b6260](https://github.com/slashfi/slash-sdk-python/commit/f3b6260b5408f2e991155c007b2b84b13f164798))

## 0.1.0-alpha.1 (2025-05-23)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/slashfi/slash-sdk-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([defc219](https://github.com/slashfi/slash-sdk-python/commit/defc2195b9414cca95fa00887cc17ce384200534))


### Chores

* update SDK settings ([f00a22b](https://github.com/slashfi/slash-sdk-python/commit/f00a22bc7b33f7c323155e243cf3a8731ec81e77))
* update SDK settings ([f4f4a22](https://github.com/slashfi/slash-sdk-python/commit/f4f4a2231d99b105cb4eb8117ee0589bf5290b01))
* update SDK settings ([9041231](https://github.com/slashfi/slash-sdk-python/commit/90412312699787194863b1a20366617e2df59466))
