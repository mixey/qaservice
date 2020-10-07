SET session vars.first_name = '{{ firstname }}';
SET session vars.last_name = '{{ lastname }}';
SET session vars.contractor_name = '{{ contractor_name }}';
SET session vars.phone = '{{ phone }}';
SET session vars.email = '{{ email }}';
SET session vars.is_email_verified = {{ is_email_verified }};
SET session vars.address_title = '{{ address_name }}';
SET session vars.address_count = {{ address_count }};
SET session vars.address_not_confirmed_count = {{ address_not_confirmed_count }};
SET session vars.inn = '{{ inn }}';

INSERT INTO public.user_profile (first_name, last_name, second_name, email, is_email_verified, phone, is_phone_verified, is_active, settings, creator_id, updater_id, date_created, date_updated, contractor_id)
VALUES (current_setting('vars.first_name'), current_setting('vars.last_name'), null, current_setting('vars.email'), current_setting('vars.is_email_verified')::bool, current_setting('vars.phone'), false, true, '{"location_id": 508635, "subscriptions": {"offers": true}}', null, null, '2019-07-16 08:32:25.000000', '2019-07-16 08:34:26.000000', null);

INSERT INTO public.contractor (name, status, settings, is_active, type, date_created, date_updated, creator_id, updater_id, meta)
VALUES (current_setting('vars.contractor_name'), 'confirmed', '{"is_remote_control": false, "veterinary_approve": false}', true, 'individual', '2019-07-16 08:34:26.000000', null, currval('user_profile_id_seq'), null, null);

UPDATE public.user_profile
SET
    updater_id = currval('user_profile_id_seq'),
    contractor_id = currval('contractor_id_seq')
WHERE id = currval('user_profile_id_seq');

INSERT INTO public.user_identity (identity, credential, user_profile_id, creator_id, updater_id, date_created, date_updated, type)
VALUES (current_setting('vars.email'), '$2y$12$HfzAIwKcGlg7EW3C.OooN.yheaM3HW2bP/zm52jobVvaM9MXgQg5i', currval('user_profile_id_seq'), currval('user_profile_id_seq'), null, '2019-07-16 08:32:25.000000', '2019-08-04 16:30:10.000000', 1);

INSERT INTO public.user_role (user_id, role_name, active_from, active_to, creator_id, updater_id, date_created, date_updated)
VALUES (currval('user_profile_id_seq'), 'member', '2019-07-16 08:32:25.070120', null, currval('user_profile_id_seq'), null, '2019-07-16 08:32:25.000000', null);

INSERT INTO public.delivery_address (status, contractor_id, title, geo, address, porch, floor, flat, contact_firstname, contact_phone, contact_lastname, comment, is_default, is_accurate, meta, date_created, date_updated, creator_id, updater_id, _disable_update_trigger, is_geo_need_update, owner_id)
SELECT status, currval('contractor_id_seq') as contractor_id, title, geo, address, porch, floor, flat, contact_firstname, contact_phone, contact_lastname, comment, false, is_accurate, meta, date_created, date_updated, currval('user_profile_id_seq'), null, _disable_update_trigger, is_geo_need_update, currval('user_profile_id_seq')
 FROM delivery_address
 WHERE address like '%Томск%' AND is_accurate = true AND status = 2 AND title IS NOT null
 limit current_setting('vars.address_count')::int OFFSET (select floor(random() * 20 + 1));

INSERT INTO public.agreement_delivery_address (delivery_address_id, agreement_id)
SELECT id, 94 FROM delivery_address WHERE contractor_id = currval('contractor_id_seq');

INSERT INTO public.delivery_address (status, contractor_id, title, geo, address, porch, floor, flat, contact_firstname, contact_phone, contact_lastname, comment, is_default, is_accurate, meta, date_created, date_updated, creator_id, updater_id, _disable_update_trigger, is_geo_need_update, owner_id)
SELECT status, currval('contractor_id_seq') as contractor_id, title, geo, address, porch, floor, flat, contact_firstname, contact_phone, contact_lastname, comment, false, is_accurate, meta, date_created, date_updated, currval('user_profile_id_seq'), null, _disable_update_trigger, is_geo_need_update, currval('user_profile_id_seq')
 FROM delivery_address
 WHERE address like '%Томск%' AND is_accurate = true AND status = 1 AND title IS NOT null
 limit current_setting('vars.address_not_confirmed_count')::int OFFSET (select floor(random() * 20 + 1));

INSERT INTO public.requisite (inn, kpp, legal_address, contractor_id, creator_id, updater_id, date_created, date_updated)
VALUES (current_setting('vars.inn'), null, current_setting('vars.contractor_name'), currval('contractor_id_seq'), null, null, '2019-03-11 11:45:51.041275', '2020-01-21 06:50:30.000000');

INSERT INTO public.user_role (user_id, role_name, active_from, active_to, creator_id, updater_id, date_created, date_updated)
VALUES (currval('user_profile_id_seq'), 'contractor_admin', '2020-07-29 08:43:15.642310', null, null, null, '2020-07-29 08:43:15.642310', null);
