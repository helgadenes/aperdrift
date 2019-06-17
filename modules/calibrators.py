from astropy.coordinates import SkyCoord

# Standard calibrators:
# names = ['3C138', '3C147', 'CTD93', '3C286', '3C48']
cb_names = ['Cyg A']
cb_cal = [SkyCoord.from_name(name) for name in cb_names]
flux_names = ['3C147', '3C196']
flux_cal = [SkyCoord.from_name(name) for name in flux_names]
pol_names = ['3C138', '3C286', 'CTD93', '3C48']
pol_cal = [SkyCoord.from_name(name) for name in pol_names]
psr_names = ['B1933+16', 'B0531+21', 'B0329+54', 'B0950+08']
psr_cal = [SkyCoord.from_name('PSR '+name) for name in psr_names]

if __name__ == '__main__':
    print("Drift scan calibrators are:")
    for i in range(len(cb_names)):
        print('\t({}) {}: {}'.format(i, cb_names[i], cb_cal[i].to_string('hmsdms')))
    print("Flux calibrators are:")
    for i in range(len(flux_names)):
        print('\t({}) {}: {}'.format(i, flux_names[i], flux_cal[i].to_string('hmsdms')))
    print("Polarization calibrators are:")
    for i in range(len(pol_names)):
        print('\t({}) {}: {}'.format(i, pol_names[i], pol_cal[i].to_string('hmsdms')))
    print("Pulsar calibrators are:")
    for i in range(len(psr_names)):
        print('\t({}) {}: {}'.format(i, psr_names[i], psr_cal[i].to_string('hmsdms')))